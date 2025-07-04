from django.db import models
from django.contrib.auth.models import User
from .models import Dish

# Create your models here.

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return f"Замовлення {self.id} {self.user.username} - {'Завершено' if self.is_completed else 'Очікує'}"
    
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)    

    def __str__(self):
        return f"{self.quantity} x {self.dish.name} для замовлення {self.order.id}"