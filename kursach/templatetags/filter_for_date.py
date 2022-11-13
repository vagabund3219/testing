from django import template

register = template.Library()

def key(item, type_name):
    try:
        return type_name in str(type(item))
    except KeyError:
        return None
register.filter('type', key)