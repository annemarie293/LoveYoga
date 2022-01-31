from django.shortcuts import (render, reverse, redirect,
                              get_object_or_404, HttpResponse)
from django.contrib import messages
from shop.models import ShopProducts
from classes.models import YogaClass

# Create your views here.


def view_basket(request):
    """ A view to return the page displaying all the shop products"""

    basket = request.session.get('basket', {})
    context = {
        'basket': basket
    }
    return render(request, 'basket/view_basket.html', context)


def add_product_to_basket(request, item_id):
    """ Add a class or a quantity of the specified product to the basket"""

    product = get_object_or_404(ShopProducts, id=item_id)
    quantity = int(request.POST.get('quantity'))
    category = request.POST.get('category')
    unique_id = category + item_id
    redirect_url = request.POST.get('redirect_url')
    basket = request.session.get('basket', {})

    if unique_id in list(basket.keys()):
        basket[unique_id]['quantity'] += quantity
        messages.success(request,
                         f'You now have {basket[unique_id]["quantity"]}\
                          x {product.name} in your basket')
    else:
        basket[unique_id] = {'item_id': item_id,
                             'quantity': quantity,
                             'category': category}
        messages.success(request,
                         f'{product.name} is now added to your basket')

    request.session['basket'] = basket
    return redirect(redirect_url)


def add_class_to_basket(request, item_id):
    """ Add a class to the basket"""
    classes = get_object_or_404(YogaClass, id=item_id)
    quantity = int(request.POST.get('quantity'))
    category = request.POST.get('category')
    unique_id = category + item_id
    redirect_url = request.POST.get('redirect_url')
    basket = request.session.get('basket', {})

    if unique_id in list(basket.keys()):
        messages.info(request, f"It looks like youve already added\
                                {classes.name} to your basket!")
    else:
        basket[unique_id] = {'item_id': item_id,
                             'quantity': quantity,
                             'category': category}
        messages.success(request,
                         f'{classes.name} is now added to your basket')

    request.session['basket'] = basket
    return redirect(redirect_url)


def update_basket(request, unique_id):
    """ Update product qty from basket page"""

    quantity = int(request.POST.get('quantity'))
    basket = request.session.get('basket', {})

    item_id = basket[unique_id]['item_id']
    product = get_object_or_404(ShopProducts, id=item_id)
    
    if basket[unique_id]['category'] == "product":
        if quantity > 0:
            basket[unique_id]['quantity'] = quantity
            messages.success(request,
                             f'Item quantity has been updated to {quantity}')
        else:
            basket.pop(unique_id)
            messages.success(request,
                             f'{product.name}'
                             ' has been removed from your basket')

    request.session['basket'] = basket
    return redirect(reverse('view_basket'))


def remove_from_basket(request, unique_id):
    """ Remove product or class from basket """
    basket = request.session.get('basket', {})
    item_id = basket[unique_id]['item_id']
    try:
        if basket[unique_id]['category'] == "product":
            product = get_object_or_404(ShopProducts, id=item_id)
            basket.pop(unique_id)
            messages.success(request,
                             f'{product.name}'
                             ' has been removed from your basket')
        elif basket[unique_id]['category'] == "class":
            classes = get_object_or_404(YogaClass, id=item_id)
            basket.pop(unique_id)
            messages.success(request,
                             f'{classes.name}'
                             ' has been removed from your basket')

        request.session['basket'] = basket
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
