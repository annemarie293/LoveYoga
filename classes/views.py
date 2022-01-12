from django.shortcuts import render
from .models import YogaClass

# Create your views here.


def classes(request):
    """ A view to return the page displaying the yoga classes """

    classes = YogaClass.objects.all()

    context = {
        'classes': classes,
    }

    return render(request, 'classes/classes.html', context)