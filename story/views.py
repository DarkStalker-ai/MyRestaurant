from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Order, OrderItem, Dish

# Create your views here.
@login_required
def create_order(request):

    order = Order.objects.create(user=request.user)
    return redirect('dish_list', order_id=order.id)

@login_required
def add_to_order(request, dish_id):
    dish = get_object_or_404(Dish, id=dish_id)
    order, created = Order.objects.get_or_create(user=request.user, is_completed=False)

    order_item, created = OrderItem.objects.get_or_create(
        order=order,
        dish=dish,
        defaults={'price': dish.price}
    )

    if not created:
        order_item.quantity += 1
        order_item.save()

    return redirect('order_detail', order_id=order.id)

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
def order_history(request):
    orders = Order.objects.filter(user=request.user, is_completed=True)
    return render(request, 'story/order_history.html', {'orders': orders})