from videopath.apps.users.models import User, UserProfile
from django.conf import settings

from rest_framework import serializers

from videopath.apps.files.util import thumbnails_util
from videopath.apps.users.models import UserSettings, Team, TeamMember

#
#
#
class UserSettingsSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserSettings

class FullProfileSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(min_length=2, required=True)
    last_name = serializers.CharField(min_length=2, required=True)
    phone = serializers.CharField(min_length=10, required=True, allow_blank=True) 
    gender = serializers.CharField(min_length=1, required=True)
    occupation = serializers.CharField(required=True, allow_blank=True)
    industry = serializers.IntegerField(required=False)
    industry_other = serializers.CharField(required=False, allow_blank=True)
    birthdate = serializers.DateField(required=True)
    avatar = serializers.SerializerMethodField()

    class Meta:
        model = UserProfile 
        fields = ('avatar', 'first_name', 'last_name', 'phone', 'gender', 'occupation', 'industry', 'industry_other', 'birthdate', 'ref')
        read_only_fields = ('ref',)

    def get_avatar(self, profile):
        return thumbnails_util.thumbnails_for_profile(profile)

    def validate(self, data):
        if data['industry'] == 999 and not data['industry_other']:
            raise serializers.ValidationError({'industry_other': "Industry should be specified when \"Other\" is selected."}) 
        return data

class ProfileSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(min_length=2, required=True)
    last_name = serializers.CharField(min_length=2, required=True)

    class Meta:
        model = UserProfile 
        fields = ('avatar', 'first_name', 'last_name', 'ref')
        read_only_fields = ('ref',)

#
#
#
class UserSerializer(serializers.ModelSerializer):
    profile = serializers.SerializerMethodField()

    plan = serializers.SerializerMethodField()
    username = serializers.CharField(min_length=3, required=False)

    newsletter = serializers.BooleanField(required=False)

    password = serializers.CharField(min_length=6, required=False, write_only=True)
    new_password = serializers.CharField(min_length=6, required=False)

    def get_plan(self, user):
        plan = "free-free"
        try:
            plan = user.subscription.plan
        except:
            pass
        return settings.PLANS.get(plan, settings.DEFAULT_PLAN)

    def get_profile(self, user):
        if hasattr(user, 'profile'):
            profile = user.profile
            return {
                "first_name": profile.first_name,
                "last_name": profile.last_name,
                "ref": profile.ref,
                "avatar": thumbnails_util.thumbnails_for_profile(profile)['regular']
            }
        return {}


    class Meta:
        model = User
        fields = ('username', 'default_team', 'email', 'id', 'plan', 'url', 'new_password','password', 'newsletter', 'profile')
        read_only_fields = ('username', 'id', 'default_team', 'first_name','last_name', 'profile')


class SlimUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'id')
        read_only_fields = ('username', 'id', 'email')

#
#
#
class TeamSerializer(serializers.ModelSerializer):

    role = serializers.SerializerMethodField()
    is_default_team = serializers.SerializerMethodField()

    detect_cover = serializers.SerializerMethodField() # use this for auto-cover selection (read-only)
    actual_cover = serializers.SerializerMethodField() # user this for returning actual cover no matter what

    stats = serializers.SerializerMethodField()

    owner = SlimUserSerializer(read_only=True)

    plan = serializers.SerializerMethodField()

    def get_plan(self, team):
        plan = "free-free"
        try:
            plan = team.owner.subscription.plan
        except:
            pass
        return settings.PLANS.get(plan, settings.DEFAULT_PLAN)

    # todo
    def get_role(self, team):
        user = self.context.get('request').user
        if team.is_user_owner(user): return 'owner'
        if team.is_user_admin(user): return 'admin'
        if team.is_user_member(user): return 'editor'
        return None

    def get_detect_cover(self, team):
        active_videos = team.videos.filter(archived=False).order_by('pk')
        if active_videos.count() > 0:
            for vid in active_videos: # hit first existing thmbnail
                revision = vid.draft
                large = thumbnails_util.thumbnails_for_revision(revision)['large']
                if large:
                    return large
        thumb = thumbnails_util.thumbnails_for_project(team)['regular']
        if thumb:
            return thumb
        return None

    def get_actual_cover(self, team):
        return thumbnails_util.thumbnails_for_project(team)['regular']

    def get_is_default_team(self, team):
        return team.is_a_default_team() 

    def get_stats(self, team):
        return {
            "number_of_videos": team.videos.filter(archived=False).count(),
            "number_of_members": team.members.count()
        }

    class Meta:
        model = Team
        fields = ('owner', 'name', 'description', 'id', 'role', 'is_default_team', 'stats', 'created', 'plan', 'detect_cover', 'actual_cover')
        read_only_fields = ('owner', 'stats', 'created', 'detect_cover')


#
#
#
class TeamMemberSerializer(serializers.ModelSerializer):
    email = serializers.SerializerMethodField()

    def get_email(self, member):
        return member.user.email

    class Meta:
        model = TeamMember
        fields = ('user', 'team', 'role', 'email', 'created', 'id')
        read_only_fields = ('user', 'team', 'email', 'created')
