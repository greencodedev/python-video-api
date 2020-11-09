# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models

import random, string

def create_profiles(apps, schema_editor):
    # We can't import the Person model directly as it may be a newer
    # version than this migration expects. We use the historical version.
    UserProfile = apps.get_model('users', 'UserProfile')
    User = apps.get_model('auth', 'User')
    for user in User.objects.filter(pk__gt=0).exclude(username='admin'):
        key8 = ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(8))
        if UserProfile.objects.filter(user=user).count() == 0:
            up = UserProfile(user=user, first_name='Videopath', last_name='User', gender='u', ref=key8)
            up.save()

class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_auto_20200426_2245'),
    ]

    operations = [
        migrations.RunPython(create_profiles),
    ]
