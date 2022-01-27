from django.urls import path
from . import views

urlpatterns = [
    path('', views.classes, name='classes'),
    path('<int:classes_id>/', views.class_info, name='class_info'),
    path('add/', views.add_class, name='add_class'),
]