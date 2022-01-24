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
        print(intent)
        return HttpResponse(
            content=f'Webhook recieved: {event["type"]}', status=200
        )

    def handle_payment_intent_payment_failed(self, event):
        """
        To handle payment_intent_payment_failed webhook from stripe
        """
        return HttpResponse(
            content=f'Webhook recieved: {event["type"]}', status= 200
        )