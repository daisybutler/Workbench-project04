from django.shortcuts import render, get_object_or_404
from .models import UserProfile
from .forms import UserProfileForm
from django.contrib import messages
from checkout.models import Order


def profile(request):
    """Display user's profile"""

    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')

    form = UserProfileForm(instance=profile)
    orders = profile.purchases.all()
    for order in orders:
        item = Order.objects.get(order_id=order)

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'profile': profile,
        'orders': orders,
        'item': item,
    }

    return render(request, template, context)


def order_history(request, order_id):

    order = get_object_or_404(Order, order_id=order_id)
    print(type(order_id))
    print(order)

    context = {
        'order': order,
    }

    template = {
        'profiles/order-history.html'
    }

    return render(request, template, context)
