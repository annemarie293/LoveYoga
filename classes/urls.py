from django.urls import path
from . import views

urlpatterns = [
    path('', views.classes, name='classes'),
    path('<int:classes_id>/', views.class_info, name='class_info'),
]