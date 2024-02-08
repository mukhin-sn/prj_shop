from django import template

from config.settings import MEDIA_ROOT, MEDIA_URL

register = template.Library()


@register.simple_tag()
def media_path(var):
    return f"/media/{var}"


@register.filter()
def path_media(var):
    return f"/media/{var}"
