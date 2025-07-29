from django.shortcuts import render, get_object_or_404
from .models import Dish

# Create your views here.

def menu(request):
    return render(request, 'menu/menu.html')

def dish_list(request):
    dishes = Dish.objects.all()
    categories = Dish.CATEGORIES_CHOICES
    
    return render(request, '../templates/menu/dish_list.html', {
        'dishes': dishes,
        'categories': categories
    })

def dish_detail(request, pk):
    dish = get_object_or_404(Dish, pk=pk)
    return render(request, '../templates/menu/dish_details.html', {'dish': dish})

def dish_list_by_category(request, category):
    dishes = Dish.objects.filter(category=category, available=True)
    category_name = dict(Dish.CATEGORIES_CHOICES).get(category, "Unknown Category")
    return render(request, 'menu/dish_list_by_category.html', {'dishes': dishes, 'category': category_name})