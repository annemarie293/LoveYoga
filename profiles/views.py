from django.shortcuts import render

# Create your views here.


def profile(request):
    """
    A view to display the user profile page
    """
    template = 'profiles/profile.html'

    context = {}

    return render(request, template, context)
