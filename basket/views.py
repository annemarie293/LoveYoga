from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.contrib import messages
from shop.models import ShopProducts
from classes.models import YogaClass

# Create your views here.


def view_basket(request):
    """ A view to return the page displaying all the shop products"""

    context = {
    }
    return render(request, 'basket/view_basket.html', context)


def add_product_to_basket(request, item_id):
    """ Add a class or a quantity of the specified product to the basket"""

    product = get_object_or_404(ShopProducts, id=item_id)
    quantity = int(request.POST.get('quantity'))
    category = request.POST.get('category')
    redirect_url = request.POST.get('redirect_url')
    basket = request.session.get('basket', {})

   
    if item_id in list(basket.keys()):
        if category in basket[item_id]['category'] == "product":
            basket[item_id]['quantity'] += quantity
            messages.success(request, f'You now have {basket[item_id]["quantity"]} x {product.name} in your basket')
    else:
        basket[item_id] = {'quantity': quantity, 'category': category}
        messages.success(request, f'{product.name} is now added to your basket')

    request.session['basket'] = basket
    return redirect(redirect_url)

def add_class_to_basket(request, item_id):
    """ Add a class to the basket"""
    
    classes = get_object_or_404(YogaClass, id=item_id)
    quantity = int(request.POST.get('quantity'))
    category = request.POST.get('category')
    redirect_url = request.POST.get('redirect_url')
    basket = request.session.get('basket', {})
 
    if item_id in list(basket.keys()):
            if category in basket[item_id]['category'] == "class":
                basket[item_id]['quantity'] += quantity
                messages.success(request, f'You now have {basket[item_id]["quantity"]} x {classes.name} in your basket')
    else:
        basket[item_id] = {'quantity': quantity, 'category': category}
        messages.success(request, f'{classes.name} is now added to your basket')

    request.session['basket'] = basket
    return redirect(redirect_url)
