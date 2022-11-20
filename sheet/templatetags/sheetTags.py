from django import template

register = template.Library()

@register.filter(name='split')
def split(value):
    """
        Returns the value turned into a list.
    """
    return value.splitlines()

@register.filter(name='formatSource')
def formatSource(sources):
    """
        Returns the formatted version of source.
    """
    first = True
    fullString = ""
    for source, value in sources.items():
        if first:
            first = False
            string = str(value) + "(" + source + ")"
        else:
            string = " + " + str(value) + "(" + source + ")"
        
        fullString += string

    return fullString