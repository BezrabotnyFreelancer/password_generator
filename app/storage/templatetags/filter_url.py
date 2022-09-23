from django import template


register = template.Library()

@register.filter
def filter(url: str):
    return url.split('/')[2]