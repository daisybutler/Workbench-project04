from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.conf import settings

from plans.models import Plan
from .forms import CheckoutForm
from profiles.forms import UserProfileForm
from .models import Order
from profiles.models import UserProfile
from locations.models import Locations
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

from django.contrib import messages
from checkout.contexts import purchase_contents
from decimal import Decimal
import stripe
import json


def checkout_order(request, name):

    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY
    order = Plan.objects.get(name=name)
    locations = Locations.objects.all()

    if request.method == 'POST':
        purchase = request.session.get('purchase', {})
        order = Plan.objects.get(name=name)

        form_data = {
            'plan_name': request.POST['plan_name'],
            'plan_type': request.POST['plan_type'],
            'plan_friendly_name': request.POST['plan_friendly_name'],
            'location': request.POST['location'],
            'price': request.POST['price'],
            'first_name': request.POST['first_name'],
            'last_name': request.POST['last_name'],
            'email': request.POST['email'],
            'password': request.POST['password'],
            'phone_number': request.POST['phone_number'],
            'county': request.POST['county'],
            'postcode': request.POST['postcode'],
            'billing_address': request.POST['billing_address'],
        }

        checkout_form = CheckoutForm(form_data)
        if checkout_form.is_valid():
            completed_order = checkout_form.save(commit=False)
            pid = request.POST.get('client_secret').split('_secret')[0]
            completed_order.stripe_pid = pid
            completed_order.original_purchase = json.dumps(purchase)
            completed_order.save()

            username = form_data['email']
            email = form_data['email']
            password = form_data['password']

            User.objects.create_user(username, email, password)
                              
            new_user = authenticate(request,
                                    username=username,
                                    password=password,
                                    )
            if new_user is not None:
                login(request, new_user)

            return redirect(
                reverse('checkout_complete', args=[completed_order.order_id]))

        else:
            messages.error(request, 'There was an error with your form. \
                Please double check your information.')

    else:
        purchase = request.session.get('purchase', {})
        purchase['plan'] = name

        # Need to fetch the inputed qunatity by user from form
        # Need to somehow update payment intent after creation
        purchase['quantity'] = 1
        purchase['price'] = int(order.price)

        request.session['purchase'] = purchase

        if not purchase:
            messages.error(request, "Whoops, something went wrong. Please reselect a plan.")
            return redirect(reverse('all_plans'))

        total = purchase['price']
        qty = purchase['quantity']
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=round(total * 100) * qty,
            currency=settings.STRIPE_CURRENCY,
        )

        """
        if request.user.is_authenticated:
            try:
                profile = UserProfile.objects.get(user=request.user)
                checkout_form = CheckoutForm(initial={
                    'full_name': profile.user.get_full_name(),
                    'email': profile.user.email,
                    'phone_number': profile.default_phone_number,
                    'postcode': profile.default_postcode,
                    'billing_address': profile.default_billing_address,
                    'county': profile.default_county,
                })
            except UserProfile.DoesNotExist:
                checkout_form = CheckoutForm()
        else:
            checkout_form = CheckoutForm()
        """

        order = Plan.objects.get(name=name)
        checkout_form = CheckoutForm()

        if not stripe_public_key:
            messages.warning(request, 'Stripe public key is missing. \
                Did you forget to set it in your environment?')

        context = {
            'order': order,
            'locations': locations,
            'checkout_form': checkout_form,
            'stripe_public_key': stripe_public_key,
            'client_secret': intent.client_secret,
        }

        return render(request, 'checkout/checkout-order.html', context=context)


def checkout_complete(request, order_id):
    """A view that renders the order payment page"""

    member_order = get_object_or_404(Order, order_id=order_id)
    order_id = order_id

    profile = UserProfile.objects.get(user=request.user)
    # Attach user's profile to order
    member_order.user_profile = profile
    member_order.save()

    profile_data = {
            'default_first_name': member_order.first_name,
            'default_last_name': member_order.last_name,
            'default_email': member_order.email,
            'default_phone_number': member_order.phone_number,
            'default_billing_address': member_order.billing_address,
            'default_postcode': member_order.postcode,
            'default_county': member_order.county,
            }

    user_profile_form = UserProfileForm(profile_data, instance=profile)
    if user_profile_form.is_valid():
        user_profile_form.save()

    messages.success(request, f'Order successfully processed! \
    Your order ID is {order_id}. A confirmation \
    email will be sent to {member_order.email}.')

    context = {
        'member_order': member_order,
    }

    if 'purchase' in request.session:
        del request.session['purchase']

    return render(request, 'checkout/checkout-complete.html', context=context)
