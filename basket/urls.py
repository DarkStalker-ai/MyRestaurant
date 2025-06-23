from django.urls import path
from . import views


urlpatterns = [
    path('add/<int:dish_id>/', views.add_to_basket, name='add_to_basket'),
    path('', views.basket_detail, name='basket_detail'),
]