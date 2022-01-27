from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from .models import YogaClass
from .forms import ClassForm
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


def add_class(request):
    """ A view to return the admin page to add a new class """

    if request.method == 'POST':
        form = ClassForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'New class details successfully added')
            return redirect(reverse('shop'))
        else:
            messages.error(request, 'Failed to add new class.'
                                    ' Please ensure your form is valid.')
    else:
        form = ClassForm()

    template = 'classes/add_class.html'
    
    context = {
        'form': form,
    }

    return render(request, template, context)


def edit_class(request, classes_id):

    classes = get_object_or_404(YogaClass, id=classes_id)
    
    if request.method == 'POST':
        form = ClassForm(request.POST, request.FILES, instance=classes)
        if form.is_valid():
            form.save()
            messages.success(request, 'Class details successfully updated')
            return redirect(reverse('class_info', args=[classes.id]))
        else:
            messages.error(request, 'Failed to update this class.'
                                    ' Please ensure your form is valid.')

    else:
        form = ClassForm(instance=classes)
    
    template = 'classes/edit_class.html'
    context = {
        'form': form,
        'classes': classes,
    }

    return render(request, template, context)

