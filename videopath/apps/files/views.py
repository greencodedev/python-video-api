
from django.conf import settings
from django.shortcuts import get_object_or_404

from videopath.apps.videos.models import MarkerContent, VideoRevision
from videopath.apps.files.models import ImageFile
from videopath.apps.files.util.aws_util import get_upload_endpoint, verify_upload
from videopath.apps.common.services import service_provider

from rest_framework.decorators import api_view
from rest_framework.response import Response
from videopath.apps.users.models import UserProfile, Team
#
# Handle image uploads
#
@api_view(['POST', 'GET'])
def image_request_upload_ticket(request, type=None, related_id=None):
    file = ImageFile()

    # file for marker content
    if type == "marker_content":
        marker_content = get_object_or_404(MarkerContent, pk=related_id)
        if not marker_content.has_user_access(request.user):
            return Response(status=403)

        file.image_type = file.MARKER_CONTENT
        file.save()
        marker_content.image_file.add(file)
        marker_content.save()
    # file as thumbnail
    elif type == "custom_thumbnail":
        revision = get_object_or_404(VideoRevision, pk=related_id)
        if not revision.has_user_access(request.user):
            return Response(status=403)
        file.image_type = file.CUSTOM_THUMBNAIL
        file.save()
        revision.custom_thumbnail = file
        revision.save()
    elif type == "profile_avatar":
        user_profile = get_object_or_404(UserProfile, ref=related_id)
        if not user_profile.has_user_access(request.user):
            return Response(status=403)
        file.image_type = file.PROFILE_AVATAR
        file.save()
        user_profile.avatar = file
        user_profile.save()
    elif type == "project_cover":
        project = None
        if related_id != 'new':
            project = Team.objects.filter(pk=related_id, owner=request.user)
            if project.count() == 0:
                return Response(status=403)
            project = project[0]
        file.image_type = file.PROJECT_COVER
        file.save()
        if project:
            project.cover = file
            project.save()
    # unknown
    else:
        return Response(status=403)

    return Response({
        'ticket_id': file.key, 
        'endpoint': get_upload_endpoint(key=file.key),
        'marker_content_id': related_id
        })


@api_view(['POST', 'GET'])
def image_request_upload_ticket_legacy(request, content_id=None):
    return image_request_upload_ticket(request, related_id=content_id, type="marker_content")

@api_view(['POST', 'GET'])
def image_upload_complete(request, ticket_id=None):
    ifile = get_object_or_404(ImageFile, key=ticket_id)
    file_found = verify_upload(ticket_id=ticket_id)
    if file_found:
        ifile.status = ImageFile.FILE_RECEIVED
        ifile.save()
    service = service_provider.get_service("image_resize")
    service.resize_image_file(ifile)
    return Response({
        'ticket_id': ticket_id,
        'file_found': file_found,
        'file_url': settings.IMAGE_CDN + ifile.key
    })

    
