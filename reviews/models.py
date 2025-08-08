from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from menu.models import Dish

# Create your models here.
class Review(models.Model):
    RATING_CHOICES = [
        (1, '1 — Погано'),
        (2, '2 — Не дуже'),
        (3, '3 — Нормально'),
        (4, '4 — Добре'),
        (5, '5 — Чудово'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE, related_name='reviews')
    rating = models.IntegerField(choices=RATING_CHOICES)
    comment = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Review by {self.user.username} for {self.dish.name} - Rating: {self.rating}'

@receiver(post_save, sender=Review)
def update_dish_popularity(sender, instance, created, **kwargs):
    if created:
        instance.dish.update_popularity()