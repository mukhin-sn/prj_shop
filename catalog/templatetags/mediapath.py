from django import template


register = template.Library()


@register.simple_tag()
def mediapath():
    pass


@register.filter()
def mediapath():
    pass