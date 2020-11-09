
from django.conf import settings

from videopath.apps.files.settings import image_sizes

thumbnail_interval = 60


# get thumb
# helpers
def thumbnails_for_video( video):
    return thumbnails_for_revision(video.current_revision)

def thumbnails_for_revision( revision):

    # try custom thumbnail
    try:
        conf = image_sizes[revision.custom_thumbnail.image_type]
        result = {}
        for out in conf["outs"]:
            result[out["name"]] = settings.IMAGE_CDN + \
                out["key"].replace(
                    "_FILEKEY_", revision.custom_thumbnail.key)
        return result
    except:
        pass

    # try video source
    try:
        return revision.source.get_thumbnails()
    except:
        pass


    return {
            "normal": "",
            "large": ""
        }

def thumbnails_for_profile(profile):
    try: 
        conf = image_sizes[profile.avatar.image_type]
        result = {}
        for out in conf["outs"]:
            result[out["name"]] = settings.IMAGE_CDN + \
                out["key"].replace(
                    "_FILEKEY_", profile.avatar.key)
        return result
    except:
        pass

    return {
            "regular": ""
        }

def thumbnails_for_project(project):
    try: 
        conf = image_sizes[project.cover.image_type]
        result = {}
        for out in conf["outs"]:
            result[out["name"]] = settings.IMAGE_CDN + \
                out["key"].replace(
                    "_FILEKEY_", project.cover.key)
        return result
    except:
        pass

    return {
            "regular": ""
        }
