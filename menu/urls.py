from django.urls import path
from . import views

urlpatterns = [
    path('', views.popular_dishes, name='popular_dishes'),
    path('menu/', views.menu, name='menu'),
    path('menu/category/<str:category>/', views.dish_list_by_category, name='dish_list_by_category'),
    path('menu/dish/<int:pk>/', views.dish_detail, name='dish_details'),
]