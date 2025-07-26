from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Order, OrderItem
from django.contrib import messages
from .forms import CheckoutForm
from menu.models import Dish

# Create your views here.
@login_required
def create_order_from_basket(request):
    basket = request.session.get('basket', {})
    if not basket:
        messages.warning(request, "Ваш кошик порожній.")
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
    messages.success(request, "Ваше замовлення успішно створено!")
    return redirect('checkout', pk=order.id)
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
    total_price = sum(item.price * item.quantity for item in order.items.all())
    return render(request, 'story/order_detail.html', {'order': order, 'total_price': total_price})

@login_required
def complete_order(request, pk):
    order = Order.objects.get(pk=pk, user=request.user)
    order.is_completed = True
    order.save()
    return redirect('checkout', pk=order.pk)

@login_required
def order_story(request):
    orders = Order.objects.filter(user=request.user, is_completed=True)
    return render(request, 'story/order_story.html', {'orders': orders})

@login_required
def checkout(request, pk):
    if pk:
        order = Order.objects.get(id=pk)
        total_price = sum(item.price * item.quantity for item in order.items.all())
    else:
        order = None
        total_price = 0
    

    if request.method == 'POST':
        form = CheckoutForm(request.POST)
        if form.is_valid():
            if not order:
                order = Order.objects.create(
                    user=request.user,
                    is_completed=False
                )
            order.full_name = form.cleaned_data['full_name']
            order.phone = form.cleaned_data['phone']
            order.address = form.cleaned_data['address']
            order.payment_method = form.cleaned_data['payment_method']
            order.is_completed=True
            order.save()

            basket = request.session.get('basket', {})
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
    else:
        form = CheckoutForm()

    return render(request, 'story/checkout.html', {'form': form, 'order': order, 'total_price': total_price})