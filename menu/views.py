from django.shortcuts import render, get_object_or_404
from .models import Dish

# Create your views here.

def menu(request):
    dishes = Dish.objects.all()
    categories = Dish.CATEGORIES_CHOICES
    
    return render(request, 'menu/menu.html', {
        'dishes': dishes,
        'categories': categories
    })

def dish_detail(request, pk):
    dish = get_object_or_404(Dish, pk=pk)
    reviews = dish.reviews.all().order_by('-created_at')
    return render(request, 'menu/dish_details.html', {'dish': dish, 'reviews': reviews})

def dish_list_by_category(request, category):
    dishes = Dish.objects.filter(category=category, available=True)
    category_name = dict(Dish.CATEGORIES_CHOICES).get(category, "Unknown Category")
    return render(request, 'menu/dish_list_by_category.html', {'dishes': dishes, 'category': category_name})

def popular_dishes(request):
    popular_dishes = Dish.get_popular_dishes()
    return render(request, 'menu/popular_dishes.html', {'popular_dishes': popular_dishes})