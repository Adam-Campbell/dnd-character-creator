from django import template

register = template.Library()

@register.filter
def value_class(value):
    if value > 0:
        return 'bg-success'
    elif value < 0:
        return 'bg-danger'
    else:
        return 'bg-light text-dark'