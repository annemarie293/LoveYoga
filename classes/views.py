from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import YogaClass, Practice
from trainers.models import Trainer
from .forms import ClassForm
# Create your views here.


def classes(request):
    """ A view to return the page displaying the yoga classes """

    classes = YogaClass.objects.all()
    trainer_list = Trainer.objects.all()
    practices = Practice.objects.all()
    trainer = None
    practice = None
    query = None

    if request.GET:
        if 'trainer' in request.GET:
            trainer = str(request.GET['trainer'])
            classes = classes.filter(trainer__name=trainer)

        if 'practice' in request.GET:
            practice = str(request.GET['practice'])
            classes = classes.filter(practice__name=practice)
            
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request,
                               'Whoops! you didnt enter any class to search')

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            classes = classes.filter(queries)

    context = {
        'classes': classes,
        'trainer_list': trainer_list,
        'trainer': trainer, 
        'practices': practices,
        'practice': practice,
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
            return redirect(reverse('classes'))
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

