from django import template

register = template.Library()

@register.filter(name='split')
def split(value):
    """
        Returns the value turned into a list.
    """
    return value.splitlines()

@register.filter
def kebab(value):
    return value.replace(" ","-")
    
@register.filter
def formatTableJS(text):
    text = repr(str(text['text']))
    text = text.replace("\\n", "\\")
    
    return text

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
            if type(value) == int and value < 0:
                value = str(value).split("-")[1]
                string = " - " + value + "(" + source + ")"
            elif type(value) == int and value == 0:
                continue
            else:
                string = " + " + str(value) + "(" + source + ")"
        
        fullString += string

    return fullString