from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import YogaClass

# Create your views here.


def classes(request):
    """ A view to return the page displaying the yoga classes """

    classes = YogaClass.objects.all()

    context = {
        'classes': classes,
    }

    return render(request, 'classes/classes.html', context)


def class_info(request, classes_id):
    """ A view to show full details for each class """

    classes = get_object_or_404(YogaClass, id=classes_id)

    context = {
        'classes': classes,
    }

    return render(request, 'classes/class_info.html', context)