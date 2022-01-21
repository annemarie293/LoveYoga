from django.shortcuts import render, reverse, redirect, get_object_or_404
from shop.models import ShopProducts
from classes.models import YogaClass

# Create your views here.


def view_basket(request):
    """ A view to return the page displaying all the shop products"""

    context = {
    }

    return render(request, 'basket/view_basket.html', context)


def add_product_to_basket(request, item_id):
    """ Add a quantity of the specified product to the basket"""

    product = get_object_or_404(ShopProducts, id=item_id)
    c_or_p = product.class_or_product
    item_id = c_or_p + item_id
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    basket = request.session.get('basket', {})

   
    if item_id in list(basket.keys()):
        basket[item_id] += quantity
        # messages.success(request, f'{product.name} quantity is increased to {basket[item_id]}')
    else:
        basket[item_id] = quantity
        # messages.success(request, f'{product.name} is now added to your basket')

    request.session['basket'] = basket
    print(basket)
    return redirect(redirect_url)

def add_class_to_basket(request, item_id):
    """ Add a quantity of the specified class to the basket"""

    classes = get_object_or_404(YogaClass, id=item_id)
    c_or_p = classes.class_or_product
    item_id = c_or_p + item_id
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    basket = request.session.get('basket', {})

   
    if item_id in list(basket.keys()):
        basket[item_id] += quantity
        # messages.success(request, f'{classes.name} quantity is increased to {basket[item_id]}')
    else:
        basket[item_id] = quantity
        # messages.success(request, f'{classes.name} is now added to your basket')

    request.session['basket'] = basket
    print(basket)
    return redirect(redirect_url)