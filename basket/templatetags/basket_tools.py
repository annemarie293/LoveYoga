from django import template


register = template.Library()


@register.filter(name='line_subtotal')
def line_subtotal(price, quantity):
    return price * quantity