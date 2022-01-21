from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from shop.models import ShopProducts
from classes.models import YogaClass


def basket_contents(request):

    basket_items = []
    total = 0
    item_count = 0
    basket = request.session.get('basket', {})

           #  classes = get_object_or_404(YogaClass, id=classes_id)
           #  product = get_object_or_404(ShopProducts, id=product_id)

    
    delivery = 5

    grand_total = total + delivery

    context = {
        'bsket_items': basket_items,
        'total': total,
        'item_count': item_count,
        'delivery': delivery,
        'grand_total': grand_total,
    }

    return context