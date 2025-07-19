from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Order, OrderItem
from .forms import CheckoutForm
from menu.models import Dish

# Create your views here.
@login_required
def create_order_from_basket(request):
    basket = request.session.get('basket', {})
    if not basket:
        return redirect('basket_detail')

    order = Order.objects.create(user=request.user, is_completed=False)

    for item in basket.values():
        dish = get_object_or_404(Dish, name=item['name'])
        OrderItem.objects.create(
            order=order,
            dish=dish,
            quantity=item['quantity'],
            price=item['price']
        )

    request.session['basket'] = {}
    return redirect('order_detail', order_id=order.id)
# def add_to_order(request, dish_id):
#     dish = get_object_or_404(Dish, id=dish_id)
#     order, created = Order.objects.get_or_create(user=request.user, is_completed=False)

#     order_item, created = OrderItem.objects.get_or_create(
#         order=order,
#         dish=dish,
#         defaults={'price': dish.price}
#     )

#     if not created:
#         order_item.quantity += 1
#         order_item.save()

#     return redirect('order_detail', order_id=order.id)

@login_required
def order_detail(request, order_id):
    order = get_object_or_404(Order, pk=order_id, user=request.user)
    return render(request, 'story/order_detail.html', {'order': order})

@login_required
def complete_order(request, order_id):
    order = get_object_or_404(Order, pk=order_id, user=request.user)
    order.is_completed = True
    order.save()
    return redirect('order_detail', order_id=order.id)

@login_required
def order_story(request):
    orders = Order.objects.filter(user=request.user, is_completed=True)
    return render(request, 'story/order_story.html', {'orders': orders})