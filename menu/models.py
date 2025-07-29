from django.db import models

# Create your models here.
class Dish(models.Model):
    CATEGORIES_CHOICES = [
        ("salads", "Салати"),
        ("soups", "Супи"),
        ("main_courses", "Основні страви"),
        ("desserts", "Десерти"),
        ("beverages", "Напої"),
    ]
    name = models.CharField(max_length=100)
    description = models.TextField()
    category = models.CharField(max_length=50, choices=CATEGORIES_CHOICES)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    # resturant = models.ForeignKey(
    #     'restaurants.Restaurant', on_delete=models.CASCADE, related_name='dishes'
    # )
    available = models.BooleanField(default=True)
    image = models.ImageField(upload_to='dishes/', blank=True, null=True)
    is_popular = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    
    @classmethod
    def get_popular_dishes(cls):
        return cls.objects.filter(is_popular=True, available=True).order_by('-id')[:5]
