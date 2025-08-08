from django.urls import path
from . import views

urlpatterns = [
    path('dish/<int:dish_id>/add_review/', views.add_review, name='add_review'),
    path('dish/<int:dish_id>/reviews/', views.view_reviews, name='view_reviews'),
    path('review/<int:review_id>/delete/', views.delete_review, name='delete_review'),
]
