from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib.auth.models import User
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


@login_required
def account_delete(request, profile):
    try:
        u = User.objects.get(username=profile)
        u.delete()
        messages.success(request, "Your profile has been successfully deleted.")

    except User.DoesNotExist:
        messages.error(request, "User does not exist")
        return render(request, 'front.html')

    except Exception as e:
        return render(request, 'home', {'err':e.message})

    return redirect(reverse('home'))
