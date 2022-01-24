import stripe

from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.conf import settings
from .forms import OrderForm

from shop.models import ShopProducts
from classes.models import YogaClass
from .models import Order, OrderLineItem
from basket.contexts import basket_contents

# Create your views here.

def checkout(request):
    """
    A view to display the checkout page
    """
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        basket = request.session.get('basket', {})

        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'street_address1': request.POST['street_address1'],
            'street_address2': request.POST['street_address2'],
            'town_or_city': request.POST['town_or_city'],
            'county': request.POST['county'],
            'postcode': request.POST['postcode'],
            'country': request.POST['country'],
        }

        order_form = OrderForm(form_data)
        if order_form.is_valid():
            print('AAAAAAAAAAAAAAAAAAAA   ORDER IS VALID AAAAAAAAAAAAAAAAAAAAAAA')
            print(order_form.errors)
            order = order_form.save(commit=False)
            # pid = request.POST.get('client_secret').split('_secret')[0]
            # order.stripe_pid = pid
            # order.original_bag = json.dumps(bag)
            order.save()
            for item_id, item_data in basket.items():
                category = item_data['category']
                try:
                    if category == 'class':
                        print('AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA')
                        quantity = item_data['quantity']
                        print(quantity)
                        classes = get_object_or_404(YogaClass, id=item_id)
                        print(classes)
                        order_line_item = OrderLineItem(
                            order=order,
                            category=category,
                            product='null',
                            classes=classes,
                            quantity=quantity,
                        )
                        print(order_line_item)
                        order_line_item.save()
                        print ("ppppppppppppp order line is saved ppppppppppppp")
                    elif category == 'product':
                        print('BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB')
                        quantity = item_data['quantity']
                        products = get_object_or_404(ShopProducts, id=item_id)
                        order_line_item = OrderLineItem(
                            order=order,
                            category=category,
                            product= product,
                            classes='null',
                            quantity=quantity,
                        )
                        order_line_item.save()
                except:
                    # messages.error(request, (
                    #     "It looks like we can't process this order"
                    #     "Please contact us for more help")
                    # )
                    print ("XXXXXXXXXXXXXXXX  Did not try orderLines   XXXXXXXXXXXXXXXXX")
                    order.delete()
                    return redirect(reverse('view_basket'))

            # Save the info to the user's profile if all is well
            request.session['save_info'] = 'save-info' in request.POST
            return redirect(reverse('checkout_success', args=[order.order_number]))
        else:
            print ("XXXXXXXXXXXXXXXX  ORDER IS NOT VALID XXXXXXXXXXXXXXXXX")
            messages.error(request, 'There was an error with your form. \
                Please double check your information.')
    else:
        basket = request.session.get('basket', {})
        print ("QQQQQQQQQQQQQQQQ   whats wrong QQQQQQQQQQQQQQQQQQqq")
        if not basket:
            # messages.error(request, "You havent added anything to your basket yet!")
            return redirect(reverse('classes'))

    current_basket = basket_contents(request)
    total = current_basket['grand_total']

    stripe_total = round(total * 100)
    stripe.api_key = stripe_secret_key

    intent = stripe.PaymentIntent.create(
        amount=stripe_total,
        currency=settings.STRIPE_CURRENCY,
        payment_method_types=['card'],
    )

    print(intent)
    order_form = OrderForm()
    
    
    # if not stripe_public_key:
        # messages.warning(request, "no public key found, please check")

    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret
    }

    return render (request, 'checkout/checkout.html', context)


def checkout_success(request, order_number):
    """
    A view to display successful orders
    """

    save_info = request.session.get('save_info')
    order = get_object_or_404(Order, order_number=order_number)

    # messgaes

    if 'basket' in request.session:
        del request.session['basket']

    template ='checkout/checkout_success.html'

    context = {
        'order': order
    }

    return render(request, template, context)