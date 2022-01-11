from django.shortcuts import render
from .models import Trainer

# Create your views here.


def trainers(request):
    """ A view to return the page displaying the yoga trainers """

    trainers = Trainer.objects.all()

    context = {
        'trainers': trainers,
    }

    return render(request, 'trainers/trainers.html', context)
