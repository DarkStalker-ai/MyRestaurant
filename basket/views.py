from multiprocessing import context
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from menu.models import Dish
# Create your views here.
@login_required
def add_to_basket(request, dish_id):
    dish = get_object_or_404(Dish, id=dish_id)
    basket = request.session.get('basket', {})

    if str(dish_id) in basket:
        basket[str(dish_id)]['quantity'] += 1

    else:
        basket[str(dish_id)] = {
            'name': dish.name,
            'description': dish.description,
            'image': dish.image.url if dish.image else None,
            'price': str(dish.price),
            'quantity': 1
        }
    
    request.session['basket'] = basket
    return redirect('basket_detail')
@login_required
def basket_detail(request):
    basket = request.session.get('basket', {})
    total_price = sum(float(item['price']) * item['quantity'] for item in basket.values())

    return render(request, 'story/basket_detail.html', {'basket': basket, 'total_price': total_price})

@login_required
def remove_from_basket(request, dish_id):
    basket = request.session.get('basket', {})
    if str(dish_id) in basket:
        del basket[str(dish_id)]
        request.session['basket'] = basket
    return redirect('basket_detail')