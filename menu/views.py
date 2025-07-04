from django.shortcuts import render, get_object_or_404
from .models import Dish

# Create your views here.

def menu(request):
    return render(request, 'menu/menu.html')

def dish_list(request):
    dishes = Dish.objects.all()

    
    return render(request, '../templates/menu/dish_list.html', {
        'dishes': dishes,
        
    })

def dish_detail(request, pk):
    dish = get_object_or_404(Dish, pk=pk)
    return render(request, '../templates/menu/dish_details.html', {'dish': dish})