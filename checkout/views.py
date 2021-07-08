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
            'price_id': request.POST['price_id'],
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

            # Create a user profile in the database
            username = form_data['first_name'] + form_data['last_name']
            email = form_data['email']
            password = form_data['password']

            user = User.objects.create_user(username, email, password)

            user.first_name = form_data['first_name']
            user.last_name = form_data['last_name']
            user.save()

            # Automatically login in new user
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
        purchase['quantity'] = 1
        purchase['price'] = int(order.price)
        purchase['price_id'] = order.price_id

        request.session['purchase'] = purchase

        if not purchase:
            messages.error(request, "Whoops, something went wrong. Please reselect a plan.")
            return redirect(reverse('all_plans'))

        total = purchase['price']
        # qty = purchase['quantity']
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=round(total * 100),
            currency=settings.STRIPE_CURRENCY,
        )

    # try:
        checkout_session = stripe.checkout.Session.create(
            success_url='https://8000-emerald-dinosaur-13zzw4f7.ws-eu11.gitpod.io/checkout/checkout-complete.html?session_id={CHECKOUT_SESSION_ID}',
            cancel_url='https://8000-emerald-dinosaur-13zzw4f7.ws-eu11.gitpod.io/plans/all_plans.html',
            payment_method_types=['card'],
            mode='subscription',
            line_items=[{
                'price': purchase['price_id'],
                'quantity': 1
            }],
            )

        if request.user.is_authenticated:
            try:
                profile = UserProfile.objects.get(user=request.user)
                checkout_form = CheckoutForm(initial={
                    'plan_name': 'pkan',
                    'plan_friendly_name': 'fjf ',
                    'plan_type': 'cjkdk ',
                    'location': 'cskjds ',
                    'price': ' dkjsjkd',
                    'first_name': profile.user.get_full_name,
                    'last_name': profile.user.last_name,
                    'phone_number': profile.default_phone_number,
                    'billing_address': profile.default_billing_address,
                    'postcode': profile.default_postcode,
                    'county': profile.default_county,
                    'email': profile.user.email,
                    'password': 'password',
                })

            except UserProfile.DoesNotExist:
                checkout_form = CheckoutForm()
        else:
            checkout_form = CheckoutForm()

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
        
    # except Exception as e:
        # return messages.error(request, f'There was an error: {str(e)}')


def checkout_complete(request, order_id):
    """A view that renders the order payment page"""

    order = get_object_or_404(Order, order_id=order_id)
    # order_id = order_id

    if request.user.is_authenticated:
        profile = UserProfile.objects.get(user=request.user)
        # Attach user's profile to order
        order.user_profile = profile
        order.save()

        profile_data = {
                'default_phone_number': order.phone_number,
                'default_billing_address': order.billing_address,
                'default_postcode': order.postcode,
                'default_county': order.county,
                }

        user_profile_form = UserProfileForm(profile_data, instance=profile)
        if user_profile_form.is_valid():
            user_profile_form.save()

        messages.success(request, f'Order successfully processed! \
        Your order ID is {order_id}. A confirmation \
        email will be sent to {order.email}.')

        context = {
            'member_order': order,
        }

        if 'purchase' in request.session:
            del request.session['purchase']

        return render(request, 'checkout/checkout-complete.html', context=context)
