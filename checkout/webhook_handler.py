from django.http import HttpResponse
from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.shortcuts import get_object_or_404

from .models import Order, OrderLineItem
from shop.models import ShopProducts
from classes.models import YogaClass
from profiles.models import UserProfile

import json
import time

class StripeWH_Handler:
    """
    To handle stripe webhooks in case of crash during order submit
    """
    def __init__(self, request):
        self.request = request

    def _send_confirmation_email(self, order):
        """
        Send order confirmation email to the user
        """
        cust_email = order.email
        subject = render_to_string(
            "checkout/confirmation_emails/"
            "confirmation_email_subject.txt",
            {'order': order})
        body = render_to_string(
            "checkout/confirmation_emails/"
            "confirmation_email_body.txt",
            {'order': order,
             'contact_email': settings.DEFAULT_FROM_EMAIL})

        send_mail(
            subject,
            body,
            settings.DEFAULT_FROM_EMAIL,
            [cust_email]
        )

    def handle_event(self, event):
        """
        To handle a generic or unkown webhook event
        """
        return HttpResponse(
            content=f'Unhandled webhook recieved: {event["type"]}', status=200
        )

    def handle_payment_intent_succeeded(self, event):
        """
        To handle payment_intent.succeeded webhook from stripe
        """
        intent = event.data.object
        pid = intent.id
        basket = intent.metadata.basket
        print("1")
        print("1.b")
        print(basket)
        
        billing_details = intent.charges.data[0].billing_details
        shipping_details = intent.shipping
        grand_total = round(intent.charges.data[0].amount/100, 2)
        save_info = intent.metadata.save_info
        print("2")

        products_total = intent.metadata.products_total
        classes_total = intent.metadata.classes_total
        delivery = intent.metadata.delivery
        print("3")

        # Replace Blank shipping values with 'None'
        for field, value in shipping_details.address.items():
            if value == "":
                shipping_details.address[field] = None
        print("4")

        # Create User Profile from details in order form
        profile = None
        username = intent.metadata.username
        print("5")
        if username != 'AnonymousUser':
            profile = UserProfile.objects.get(user__username=username)
            if save_info:
                profile.default_phone_number = shipping_details.phone,
                profile.default_street_address1 = shipping_details.address.line1,
                profile.default_street_address2 = shipping_details.address.line2,
                profile.default_town_or_city = shipping_details.address.city,
                profile.default_county = shipping_details.address.state,
                profile.default_postcode = shipping_details.address.postal_code,
                profile.default_country = shipping_details.address.country,
                profile.save()
                print("6")

        # Check if order has already been created (5 times)
        order_exists = False
        print("7")
        attempt = 1
        while attempt <= 6:
            try:
                order = Order.objects.get(
                    full_name__iexact=shipping_details.name,
                    email__iexact=billing_details.email,
                    phone_number__iexact=shipping_details.phone,
                    street_address1__iexact=shipping_details.address.line1,
                    street_address2__iexact=shipping_details.address.line2,
                    town_or_city__iexact=shipping_details.address.city,
                    county__iexact=shipping_details.address.state,
                    postcode__iexact=shipping_details.address.postal_code,
                    country__iexact=shipping_details.address.country,
                    grand_total=grand_total,
                    original_basket=basket,
                    stripe_pid=pid,
                )
                order_exists = True
                break
            except Order.DoesNotExist:
                attempt += 1
                time.sleep(1)
        if order_exists: 
            print("8")
            self._send_confirmation_email(order)
            return HttpResponse(
                content=f'Webhook recieved:{event["type"]}|'
                ' SUCCESS: the verified order has been found in the database',
                status=200       
                )
        # Create order if not found in database
        else:
            order = None
            print("9")
            try:
                order = Order.objects.create(
                    user_profile=profile,
                    full_name=shipping_details.name,
                    email=billing_details.email,
                    phone_number=shipping_details.phone,
                    street_address1=shipping_details.address.line1,
                    street_address2=shipping_details.address.line2,
                    town_or_city=shipping_details.address.city,
                    county=shipping_details.address.state,
                    postcode=shipping_details.address.postal_code,
                    country=shipping_details.address.country,
                    grand_total=grand_total,
                    original_basket=basket,
                    stripe_pid=pid,
                    products_total=products_total,
                    classes_total=classes_total,
                    delivery=delivery,
                    )
                print("10")
                print("10.b")
                print(json.loads(basket).items())
                for unique_id, item_data in json.loads(basket).items():
                    category = item_data['category']
                    item_id = item_data['item_id']
                    print("item_id")
                    print(item_id)
                    print(type(item_id))
                    print("11")
                    if category == 'class':
                        quantity = item_data['quantity']
                        print("11.b")
                        print(quantity)
                        classes = get_object_or_404(YogaClass, id=item_id)
                        print(classes)
                        print("12")
                        order_line_item = OrderLineItem(
                            order=order,
                            category=category,
                            classes=classes,
                            quantity=quantity,
                        )
                        order_line_item.save() 
                        print("12.b")                
                    elif category == 'product':
                        print("12.c")
                        quantity = item_data['quantity']
                        product = get_object_or_404(ShopProducts, id=item_id)
                        print("12.d")
                        print(product)
                        order_line_item = OrderLineItem(
                            order=order,
                            category=category,
                            product=product,
                            quantity=quantity,
                        )
                        order_line_item.save()
                        print("13")
            except Exception as e:
                if order:
                    print("14")
                    order.delete()
                return HttpResponse(
                    content=f'Webhook recieved:{event["type"]}| Error: {e}',
                    status=500)
                print("15")
        self._send_confirmation_email(order)
        print("16")
        return HttpResponse(            
            content=f'Webhook received: {event["type"]} |'
            ' SUCCESS: Order created in webhook',
            status=200)
        

    def handle_payment_intent_payment_failed(self, event):
        """
        To handle payment_intent_payment_failed webhook from stripe
        """
        return HttpResponse(
            content=f'Webhook recieved: {event["type"]}', status=200
        )


