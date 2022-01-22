from django.shortcuts import get_object_or_404
from shop.models import ShopProducts
from classes.models import YogaClass


def basket_contents(request):

    basket_items = []
    classes_total = 0
    product_total = 0
    sub_total = 0
    product_count = 0
    classes_count = 0
    basket = request.session.get('basket', {})

    
    
    delivery = 5
    sub_total = classes_total + product_total
    grand_total = sub_total + delivery

    context = {
        'basket_items': basket_items,
        'sub_total': sub_total,
        'product_total': product_total,
        'classes_total': classes_total,
        'product_count': product_count,
        'classes_count': classes_count,
        'delivery': delivery,
        'grand_total': grand_total,
    }

    return context