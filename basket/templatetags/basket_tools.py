from django import template


register = template.Library()


@register.filter(name='line_subtotal')
def line_subtotal(price, quantity):
    """
    template to caluclate line subtotal in basket
    """
    return price * quantity
