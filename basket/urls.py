from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_basket, name='view_basket'),    
    path('add_product/<item_id>', views.add_product_to_basket, name='add_product_to_basket'),    
    path('add_class/<item_id>', views.add_class_to_basket, name='add_class_to_basket'),
]

