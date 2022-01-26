from django.urls import path
from . import views

urlpatterns = [
    path('', views.trainers, name='trainers'),
    path('add/', views.add_trainer, name='add_trainer'),
]