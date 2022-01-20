from django.shortcuts import render
from .models import ShopProducts

# Create your views here.


def shop(request):
    """ A view to return the page displaying the yoga classes """

    shop_products = ShopProducts.objects.all()

    context = {
        'shop_products': shop_products,
    }

    return render(request, 'shop/shop.html', context)