from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.contrib import messages
from .models import Trainer
from .forms import TrainerForm

# Create your views here.


def trainers(request):
    """ A view to return the page displaying the yoga trainers """

    trainers = Trainer.objects.all()

    context = {
        'trainers': trainers,
    }

    return render(request, 'trainers/trainers.html', context)


def add_trainer(request):
    """ A view to return the admin page to add a new trainer """

    if request.method == 'POST':
        form = TrainerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'New trainer details successfully added')
            return redirect(reverse('trainers'))
        else:
            messages.error(request, 'Failed to add new trainer.'
                                    ' Please ensure your form is valid.')
    else:
        form = TrainerForm()

    template = 'trainers/add_trainer.html'
    
    context = {
        'form': form,
    }

    return render(request, template, context)


def edit_trainer(request, trainer_id):

    trainer = get_object_or_404(Trainer, id=trainer_id)
    
    if request.method == 'POST':
        form = TrainerForm(request.POST, request.FILES, instance=trainer)
        if form.is_valid():
            form.save()
            messages.success(request, 'Trainer details successfully updated')
            return redirect(reverse('trainers'))
        else:
            messages.error(request, 'Failed to update this trainer record.'
                                    ' Please ensure your form is valid.')

    else:
        form = TrainerForm(instance=trainer)
    
    template = 'trainers/edit_trainer.html'
    context = {
        'form': form,
        'trainer': trainer,
    }

    return render(request, template, context)
