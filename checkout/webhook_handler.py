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
            content=f'Unhandled webhook recieved: {event["type"]}', status= 200
        )

    def handle_payment_intent_succeeded(self, event):
        """
        To handle a successful payment intent to stripe
        """
        return HttpResponse(
            content=f'Webhook recieved: {event["type"]}', status= 200
        )

    def handle_payment_intent_payment_failed(self, event):
        """
        To handle a failed payment intent to stripe
        """
        return HttpResponse(
            content=f'Webhook recieved: {event["type"]}', status= 200
        )