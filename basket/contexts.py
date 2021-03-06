from django.shortcuts import get_object_or_404
from shop.models import ShopProducts
from classes.models import YogaClass


def basket_contents(request):
    """
    To make basket contents available across all apps
    """

    basket_items = []
    classes_total = 0
    products_total = 0
    sub_total = 0
    products_count = 0
    classes_count = 0
    basket = request.session.get('basket', {})

    for unique_id, item_data in basket.items():
        category = item_data['category']
        item_id = item_data['item_id']
        quantity = item_data['quantity']
        if category == 'class':
            classes = get_object_or_404(YogaClass, id=item_id)
            classes_total += quantity * classes.price
            classes_count += quantity
            basket_items.append({
                'unique_id': unique_id,
                'item_id': item_id,
                'quantity': quantity,
                'category': category,
                'classes': classes
            })

        elif category == 'product':
            products = get_object_or_404(ShopProducts, id=item_id)
            products_total += quantity * products.price
            products_count += quantity
            basket_items.append({
                'unique_id': unique_id,
                'item_id': item_id,
                'quantity': quantity,
                'category': category,
                'products': products
            })

    delivery = 5
    if products_total == 0:
        delivery = 0
    sub_total = classes_total + products_total
    grand_total = sub_total + delivery

    context = {
        'basket_items': basket_items,
        'sub_total': sub_total,
        'products_total': products_total,
        'classes_total': classes_total,
        'products_count': products_count,
        'classes_count': classes_count,
        'delivery': delivery,
        'grand_total': grand_total,
    }
    return context
