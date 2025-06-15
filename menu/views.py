from django.shortcuts import render, get_object_or_404
from .models import Dish

# Create your views here.

def dish_list(request):
    dishes = Dish.objects.all()
    return render(request, '../templates/dish_list.html', {'dishes': dishes})

def dish_detail(request, pk):
    dish = get_object_or_404(Dish, pk=pk)
    return render(request, '../templates/dish_detail.html', {'dish': dish})