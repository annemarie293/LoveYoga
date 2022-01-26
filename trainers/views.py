from django.shortcuts import render, redirect, reverse
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
