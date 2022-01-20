from django.shortcuts import render, redirect, get_object_or_404
from .models import ShopProducts

# Create your views here.


def shop(request):
    """ A view to return the page displaying all the shop products"""

    shop_products = ShopProducts.objects.all()

    context = {
        'shop_products': shop_products,
    }

    return render(request, 'shop/shop.html', context)


def product_info(request, product_id):
    """ A view to show full details for the selected product in the shop """

    product = get_object_or_404(ShopProducts, id=product_id)

    context = {
        'product': product,
    }

    return render(request, 'shop/product_info.html', context)