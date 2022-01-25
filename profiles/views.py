from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from .models import UserProfile
from .forms import UserProfileForm


# Create your views here.


def profile(request):
    """
    A view to display the user profile page
    """
    profile = get_object_or_404(UserProfile, user=request.user)
    
    if request.method =='POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your new profile information has been saved')

    orders = profile.orders.all()
    print ("MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
    print(orders)

    form = UserProfileForm(instance=profile)
    template = 'profiles/profile.html'

    context = {
        'profile': profile,
        'form': form, 
        'orders': orders,
        'on_profile': True
    }

    return render(request, template, context)
