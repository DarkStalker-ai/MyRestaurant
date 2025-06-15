from django.db import models

# Create your models here.
class Category(models.Models):
    # Which is the category of the dish
    name = models.CharField(max_length=100)
    # A description of the category
    description = models.TextField(blank=True, null=True)
    # An image representing the category
    image = models.ImageField(upload_to='categories/', blank=True, null=True)

    def __str__(self):
        return self.name


class Dish(models.Models):
    name = models.CharField(max_length=100)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='dishes')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    resturant = models.ForeignKey(
        'restaurants.Restaurant', on_delete=models.CASCADE, related_name='dishes'
    )
    image = models.ImageField(upload_to='dishes/', blank=True, null=True)

    def __str__(self):
        return self.name
