from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_basket, name='view_basket'),
    path('add_product/<item_id>', views.add_product_to_basket,
         name='add_product_to_basket'),
    path('add_class/<item_id>', views.add_class_to_basket,
         name='add_class_to_basket'),
    path('update/<unique_id>', views.update_basket,
         name='update_basket'),
    path('remove/<unique_id>/', views.remove_from_basket,
         name='remove_from_basket'),
    ]
