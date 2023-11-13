from django import template


register = template.Library()


@register.filter(name='calc_subtotal')
def calc_subtotal(price, quantity):
    return price * quantity


@register.filter(name='calc_percentage')
def calc_percentage(total, free_delivery_threshold):
    return int((total / free_delivery_threshold) * 100)
