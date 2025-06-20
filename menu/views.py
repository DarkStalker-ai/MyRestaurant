from django.shortcuts import render, get_object_or_404
from .models import Dish, Category

# Create your views here.

def menu(request):
    categories = Category.objects.all()
    return render(request, '../templates/menu.html', {'categories': categories})

def dish_list(request):
    if category_id:
        category = get_object_or_404(Category, pk=category_id)
        dishes = Dish.objects.filter(category=category)
    else:
        dishes = Dish.objects.all()
        category = None

    categories = Category.objects.all()
    return render(request, '../templates/menu/dish_list.html', {
        'dishes': dishes,
        'categories': categories,
        'current_category': category
    })

def dish_detail(request, pk):
    dish = get_object_or_404(Dish, pk=pk)
    return render(request, '../templates/menu/dish_details.html', {'dish': dish})