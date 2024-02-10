from django import template

register = template.Library()


@register.simple_tag()
def media_path(path_data):
    return f"/media/{path_data}"


@register.filter()
def path_media(path_data):
    return f"/media/{path_data}"
