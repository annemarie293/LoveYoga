import stripe
import json

from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from django.contrib import messages
from django.conf import settings
from django.views.decorators.http import require_POST
from .forms import OrderForm
from profiles.forms import UserProfileForm

from shop.models import ShopProducts
from classes.models import YogaClass
from profiles.models import UserProfile
from .models import Order, OrderLineItem
from basket.contexts import basket_contents

# Create your views here.

@require_POST
def cache_checkout_data(request):
    try:
        pid = request.POST.get('client_secret').split('_secret')[0]    
        stripe_secret_key = settings.STRIPE_SECRET_KEY
        current_basket = basket_contents(request)
        products_total = current_basket['products_total']
        classes_total = current_basket['classes_total']
        stripe.PaymentIntent.modify(pid, metadata={
            'username': request.user,
            'save_info': request.POST.get('save_info'),
            'basket': json.dumps(request.session.get('basket', {})),
            'products_total':products_total, 
            'classes_total':classes_total, 
        })
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, "Sorry we can't process your payment right now, please contact us for support")
        return HttpResponse(content=e, status=400)


def checkout(request):
    """
    A view to display the checkout page
    """
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY
    
    current_basket = basket_contents(request)
    
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
            order = order_form.save(commit=False)
            order.products_total = current_basket['products_total']
            order.classes_total = current_basket['classes_total']
            pid = request.POST.get('client_secret').split('_secret')[0]
            order.stripe_pid = pid
            order.original_basket = json.dumps(basket)
            order.save()
            for item_id, item_data in basket.items():
                category = item_data['category']
                try:
                    if category == 'class':
                        quantity = item_data['quantity']
                        classes = get_object_or_404(YogaClass, id=item_id)
                        order_line_item = OrderLineItem(
                            order=order,
                            category=category,
                            classes=classes,
                            quantity=quantity,
                        )
                        order_line_item.save()                    
                    elif category == 'product':
                        quantity = item_data['quantity']
                        product = get_object_or_404(ShopProducts, id=item_id)
                        order_line_item = OrderLineItem(
                            order=order,
                            category=category,
                            product=product,
                            quantity=quantity,
                        )
                        order_line_item.save()
                except:
                    messages.error(request, (
                        "It looks like we can't process this order right now"
                        "Please contact us for more help")
                    )
                    order.delete()
                    return redirect(reverse('view_basket'))

            # Save info to the user profile if everythig is ok
            request.session['save_info'] = 'save-info' in request.POST
            return redirect(reverse('checkout_success', args=[order.order_number]))
        else:
            messages.error(request, 'There was an error with your form. \
                Please double check your information.')
    else:
        basket = request.session.get('basket', {})
        if not basket:
            messages.error(request, "You havent added anything to your basket yet!")
            return redirect(reverse('classes'))

    total = current_basket['grand_total']
    stripe_total = round(total * 100)
    stripe.api_key = stripe_secret_key

    intent = stripe.PaymentIntent.create(
        amount=stripe_total,
        currency=settings.STRIPE_CURRENCY,
        payment_method_types=['card'],
    )
    # Checks if the user is logged in and has default contact info saved
    # uses this info to prefill the order form
    if request.user.is_authenticated:
        try:
            profile = UserProfile.objects.get(user=request.user)

            order_form = OrderForm(initial={
                'full_name': profile.user.get_full_name(),
                'email': profile.user.email,
                'phone_number': profile.default_phone_number,
                'street_address1': profile.default_street_address1,
                'street_address2': profile.default_street_address2,
                'town_or_city': profile.default_town_or_city,
                'county': profile.default_county,
                'postcode': profile.default_postcode,
                'country': profile.default_country,
            })
        except UserProfile.DoesNotExist:
            order_form = OrderForm()

    else:
        order_form = OrderForm()
    
    if not stripe_public_key:
        messages.warning(request, "Stripe public key not found, please check")

    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret
    }

    return render(request, 'checkout/checkout.html', context)


def checkout_success(request, order_number):
    """
    A view to display successful orders
    """
    save_info = request.session.get('save_info')
    order = get_object_or_404(Order, order_number=order_number)

    messages.success(request, f'Order successfully processed! \
        Your order number is { order.order_number}. A confirmation \
        email will be sent to {order.email}.')

    if 'basket' in request.session:
        del request.session['basket']

    if request.user.is_authenticated:
        # Get the order profile and save it to the order
        profile = UserProfile.objects.get(user=request.user)
        order.user_profile = profile
        order.save()

        # if the 'save-info' box is saved on checkout order form
        if save_info:
            profile_data = {
                'default_phone_number': order.phone_number,
                'default_street_address1': order.street_address1,
                'default_street_address2': order.street_address2,
                'default_town_or_city': order.town_or_city,
                'default_county': order.county,
                'default_postcode': order.postcode,
                'default_country': order.country,
            }

        # Create instance of the user profile formm using above profile_data

        user_profile_form = UserProfileForm(profile_data, instance=profile)

        # use form to update the user profile
        if user_profile_form.is_valid():
            user_profile_form.save()
 
    template = 'checkout/checkout_success.html'

    context = {
        'order': order
    }

    return render(request, template, context)