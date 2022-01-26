from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.contrib import messages
from .models import ShopProducts
from .forms import ProductForm

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


def add_product(request):
    """ A view to return the admin page to add a new product """

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'New product details successfully added')
            return redirect(reverse('shop'))
        else:
            messages.error(request, 'Failed to add new product.'
                                    ' Please ensure your form is valid.')
    else:
        form = ProductForm()

    template = 'shop/add_product.html'
    
    context = {
        'form': form,
    }

    return render(request, template, context)