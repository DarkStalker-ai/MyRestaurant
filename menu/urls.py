from django.urls import path


urlpatterns = [
    path('', views.dish_list, name='dish_list'),
    path('dish/<int:pk>/', views.dish_detail, name='dish_detail'),
]