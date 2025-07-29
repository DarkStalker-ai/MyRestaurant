from django.urls import path
from . import views

urlpatterns = [
    path('', views.menu, name='menu'),
    path('menu/', views.dish_list, name='dish_list'),
    path('menu/category/<str:category>/', views.dish_list_by_category, name='dish_list_by_category'),
    path('menu/dish/<int:pk>/', views.dish_detail, name='dish_details'),
    path('', views.popular_dishes, name='popular_dishes'),
]