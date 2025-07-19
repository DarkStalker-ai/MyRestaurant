from django.urls import path
from . import views


urlpatterns = [
    # path('add_to_order/<int:dish_id>/', views.add_to_order, name='add_to_order'),
    path('order/<int:order_id>/', views.order_detail, name='order_detail'),
    path('complete_order/<int:order_id>/', views.complete_order, name='complete_order'),
    path('order_story/', views.order_story, name='order_story'),
    path('create_order_from_basket/', views.create_order_from_basket, name='create_order_from_basket'),
]