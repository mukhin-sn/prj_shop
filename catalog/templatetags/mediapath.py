from django import template

register = template.Library()


@register.simple_tag
def mediapath(path: str):
    path = "/media/" + path
    return path


# @register.simple_tag
# def sum_to_sum(var):
#     return var


@register.filter
def media_path(path):
    return f'/media/{path}'
