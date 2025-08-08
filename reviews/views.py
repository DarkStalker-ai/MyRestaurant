from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from .models import Review, Dish
from .forms import ReviewForm

# Create your views here.
def add_review(request, dish_id):
    dish = get_object_or_404(Dish, id=dish_id)
    
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.dish = dish
            review.comment = form.cleaned_data["comment"]
            review.save()
            return redirect('dish_details', pk=dish.id)
    else:
        form = ReviewForm()

    return render(request, 'reviews/add_review.html', {'form': form, 'dish': dish})

def view_reviews(request, dish_id):
    dish = get_object_or_404(Dish, id=dish_id)
    reviews = dish.reviews.all().order_by('-created_at')
    
    return render(request, 'reviews/view_reviews.html', {'dish': dish, 'reviews': reviews})

@user_passes_test(lambda u: u.is_staff)
def delete_review(request, review_id):
    review = get_object_or_404(Review, id=review_id)
    dish_id = review.dish.id
    
    if request.method == 'POST':
        review.delete()
        return redirect('view_reviews', dish_id=dish_id)

    return render(request, 'reviews/delete_review.html', {'review': review})