from django import template

register = template.Library()

@register.filter(name='split')
def split(value):
    """
        Returns the value turned into a list.
    """
    return value.splitlines()