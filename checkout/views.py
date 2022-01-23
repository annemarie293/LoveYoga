from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import OrderForm

# Create your views here.

def checkout(request):
    """
    A view to display the chekcout page
    """
    basket = request.session.get('basket', {})
    if not basket:
        # messages.error(request, "You havent added anything to your basket yet!")
        return redirect(reverse('classes'))

    order_form = OrderForm()

    context = {
        'order_form': order_form
    }

    return render (request, 'checkout/checkout.html', context)