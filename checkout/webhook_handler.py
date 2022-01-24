from django.http import HttpResponse

class StripeWH_Handler:
    """
    To handle stripe webhooks in case of crash during order submit
    """
    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """
        To handle a generic or unkown webhook even
        """
        return HttpResponse(
            content=f'Unhandled webhook recieved: {event["type"]}', status=200
        )

    def handle_payment_intent_succeeded(self, event):
        """
        To handle payment_intent_succeeded webhook from stripe
        """
        intent = event.data.object
        pid = intent.id
        basket = intent.metadata.basket
        save_info = intent.metadata.save_info
        billing_details = intent.charges.data[0].billing_details
        shipping_details = intent.shipping_details
        grand_total = round(intent.charges.data[0].amount/100, 2)

        for field, value in shipping_details.address.items():
            if value == "":
                shipping_details.address[field] = None

        order_exists = False
        attempt = 1
        while attempt <= 5:
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
                return HttpResponse(
                    content = f'Webhook recieved:{event["type"]}| SUCCESS: the verified order has been dound in the database',
                    status=200       
                    )

        else:
            order = None
            try:
                order = Order.objects.create(
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
                    )

                for item_id, item_data in json.loads(basket).items():
                    category = item_data['category']
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
            except Exception as e:
                if order:
                    order.delete()
                return HttpResponse(
                    content=f'Webhook recieved:{event["type"]}| Error: {e}',
                    status=500       
                    )     

        return HttpResponse(
            content=f'Webhook received: {event["type"]} | SUCCESS: Order created in webhook',
            status=200)

    def handle_payment_intent_payment_failed(self, event):
        """
        To handle payment_intent_payment_failed webhook from stripe
        """
        return HttpResponse(
            content=f'Webhook recieved: {event["type"]}', status= 200
        )