from django.shortcuts import render, get_object_or_404, redirect, reverse
from .models import UserProfile
from .forms import UserProfileForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from checkout.models import Order
import stripe


@login_required
def profile(request):
    """Display user's profile"""

    if request.user.is_superuser:
        messages.error(request, 'You are logged in as an administrator. Log in with a customer account to view profile.')
        return redirect(reverse('account_logout'))

    else:
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
