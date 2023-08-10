

from django import template

register = template.Library()

@register.simple_tag
def get_client_id(cliente):
    return str(cliente["_id"])

