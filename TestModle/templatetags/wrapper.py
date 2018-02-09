from django import template

register = template.Library()


@register.filter(name='getvalues')
def getvalues(obj, sele):
    return getattr(obj, sele)


@register.filter(name='getvalue')
def getvalue(obj, sele):
    return obj[int(sele)-1][1]
