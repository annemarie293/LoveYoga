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
    print('context basket')
    print(basket)

    for item_id, item_data in basket.items():
        category = item_data['category']
        if category == 'class':

            quantity = item_data['quantity']
            category = item_data['category']

            classes = get_object_or_404(YogaClass, id=item_id)
            classes_total += quantity * classes.price
            classes_count += quantity
            basket_items.append({
                'item_id': item_id, 
                'quantity': quantity,
                'category': category,
                'classes': classes
            })

        elif category == 'product':

            quantity = item_data['quantity']
            category = item_data['category']

            product = get_object_or_404(ShopProducts, id=item_id)
            product_total += quantity * product.price
            product_count += quantity
            basket_items.append({
                'item_id': item_id, 
                'quantity': quantity,
                'category': category,
                'product': product
            })
        
    delivery = 5
    sub_total = classes_total + product_total
    grand_total = sub_total + delivery

    print(sub_total)
    print(grand_total)
    print(basket_items)

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