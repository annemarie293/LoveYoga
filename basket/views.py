from django.shortcuts import render

# Create your views here.


def view_basket(request):
    """ A view to return the page displaying all the shop products"""

    context = {
    }

    return render(request, 'basket/view_basket.html', context)