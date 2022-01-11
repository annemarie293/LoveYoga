from django.urls import path
from . import views

urlpatterns = [
    path('', views.trainers, name='trainers'),
]