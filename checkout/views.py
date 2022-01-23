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
    stripe_public_key = 'pk_test_51K85HOFENeI7e0FkJtphWpl6HgVPaTD713uiD2XfcFfLlCFUFXvPecg2g7SZB6APxcRo2EPGBUwOmxcUPNAYOTx600RVp7jXTJ'
    client_secret = "test_client_secret"

    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': client_secret
    }

    return render (request, 'checkout/checkout.html', context)