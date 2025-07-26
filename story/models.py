from django.db import models
from django.contrib.auth.models import User
from menu.models import Dish

# Create your models here.

class Order(models.Model):
    PAYMENT_METHODS = [
        ('online', 'Онлайн'),
        ('cash', 'Готівка при отриманні'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100, verbose_name='Повне ім\'я', blank=True, null=True)
    phone = models.CharField(max_length=20, verbose_name='Телефон', blank=True, null=True)
    address = models.CharField(max_length=200, verbose_name='Адреса доставки', blank=True, null=True)
    payment_method = models.CharField(max_length=10, choices=PAYMENT_METHODS, verbose_name='Спосіб оплати', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Cтворено')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Оновлено')
    is_completed = models.BooleanField(default=False, verbose_name='Завершено')

    def __str__(self):
        return f"Замовлення {self.id} {self.user.username} - {'Завершено' if self.is_completed else 'Очікує'}"
    
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items', verbose_name='Замовлення')
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE, verbose_name='Страва')
    quantity = models.PositiveIntegerField(default=1, verbose_name='Кількість')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Ціна')

    def __str__(self):
        return f"{self.quantity} x {self.dish.name} для замовлення {self.order.id}"