from django.urls import path
from . import views


urlpatterns = [
    path('add/<int:dish_id>/', views.add_to_basket, name='add_to_basket'),
    path('remove/<int:dish_id>/', views.remove_from_basket, name='remove_from_basket'),
    path('', views.basket_detail, name='basket_detail'),
]