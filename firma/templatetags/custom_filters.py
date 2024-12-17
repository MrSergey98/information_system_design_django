from django import template
from django.forms.utils import flatatt

register = template.Library()

@register.filter(name='add_attr')
def add_attr(field, attr):
    attrs = {}
    definition = attr.split(':')

    if len(definition) >= 2:
        key, val = definition
        attrs.update({key.strip(): val.strip()})

    return field.as_widget(attrs=attrs)