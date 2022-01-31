from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import UserProfile
from checkout.models import Order
from .forms import UserProfileForm


# Create your views here.


@login_required
def profile(request):
    """
    A view to display the user profile page
    """
    profile = get_object_or_404(UserProfile, user=request.user)
    
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request,
                             'Your new profile information has been saved')

    orders = profile.orders.all()

    form = UserProfileForm(instance=profile)
    template = 'profiles/profile.html'

    context = {
        'profile': profile,
        'form': form, 
        'orders': orders,
        'on_profile': True
    }

    return render(request, template, context)


@login_required
def user_orders(request, order_number):
    """
    A view to display the previous order made by the user
    """
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, f'This is a record of \
                            your previous order # {order_number}')

    template = "checkout/checkout_success.html"

    context = {
        'order': order, 
        'from_profile_page': True,
    }

    return render(request, template, context)