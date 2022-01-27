from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
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


@login_required
def add_class(request):
    """ A view to return the admin page to add a new class """

    # Only superuser can access this view
    if not request.user.is_superuser:
        msgs.error(request, 'This action is restricted to site admin users')
        return redirect(reverse('home'))

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


@login_required
def edit_class(request, classes_id):

    
    # Only superuser can access this view
    if not request.user.is_superuser:
        msgs.error(request, 'This action is restricted to site admin users')
        return redirect(reverse('home'))

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


@login_required
def delete_class(request, classes_id):


    # Only superuser can access this view
    if not request.user.is_superuser:
        msgs.error(request, 'This action is restricted to site admin users')
        return redirect(reverse('home'))

    classes = get_object_or_404(YogaClass, id=classes_id)
    classes.delete()
    messages.success(request, 'Class details successfully deleted')
    return redirect(reverse('classes'))

