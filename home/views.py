from django.shortcuts import render

# Create your views here.


def index(request):
    """ A view to return the home page """
    return render(request, 'home/index.html')


def about_us(request):
    """ A view to return the About Us page """
    return render(request, 'home/about.html')
