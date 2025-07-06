from django.urls import path
from . import views

urlpatterns = [
    path('', views.menu, name='menu'),
    path('menu/', views.dish_list, name='dish_list'),
    path('menu/category/<int:pk>/', views.dish_list, name='category_detail'),
    path('menu/dish/<int:pk>/', views.dish_detail, name='dish_details'),
]