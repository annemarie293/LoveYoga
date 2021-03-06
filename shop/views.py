from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower

from .models import ShopProducts
from .forms import ProductForm

# Create your views here.


def shop(request):
    """ A view to return the page displaying all the shop products"""

    shop_products = ShopProducts.objects.all()
    query = None
    sort = None

    if request.GET:
        if 'sort' in request.GET:
            sort = request.GET['sort']
            sortkey = sort
            if sortkey == 'name':
                sortkey = 'lower_name'
                shop_products = shop_products.annotate(
                                lower_name=Lower('name'))
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            shop_products = shop_products.order_by(sortkey)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request,
                               'Whoops! you didnt enter anything to search')

            queries = Q(name__icontains=query) | Q(
                        description__icontains=query)
            shop_products = shop_products.filter(queries)

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


@login_required
def add_product(request):
    """ A view to return the admin page to add a new product """

    # Only superuser can access this view
    if not request.user.is_superuser:
        messages.error(request,
                       'This action is restricted to site admin users')
        return redirect(reverse('home'))

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


@login_required
def edit_product(request, product_id):
    """ A view to update product details in database """

    # Only superuser can access this view
    if not request.user.is_superuser:
        messages.error(request,
                       'This action is restricted to site admin users')
        return redirect(reverse('home'))

    product = get_object_or_404(ShopProducts, id=product_id)
    
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product details successfully updated')
            return redirect(reverse('product_info', args=[product.id]))
        else:
            messages.error(request, 'Failed to update this product.'
                                    ' Please ensure your form is valid.')

    else:
        form = ProductForm(instance=product)
    
    template = 'shop/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """ A view to remove a product from the database """

    # Only superuser can access this view
    if not request.user.is_superuser:
        messages.error(request,
                       'This action is restricted to site admin users')
        return redirect(reverse('home'))

    product = get_object_or_404(ShopProducts, id=product_id)
    product.delete()
    messages.success(request, 'Product details successfully deleted')
    return redirect(reverse('shop'))
