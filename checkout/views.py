from django.shortcuts import render, redirect, reverse
from django.conf import settings
from plans.models import Plan
from .models import Order
import stripe


def checkout_order(request, name):
    """A view that renders the order summary page"""

    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    purchase = request.session.get('purchase', {})
    stripe.api_key = stripe_secret_key
    intent = stripe.PaymentIntent.create(
        amount=50,
        currency=settings.STRIPE_CURRENCY,
    )

    print(intent)

    order = Plan.objects.get(name=name)

    purchase = request.session.get('purchase', {})
    purchase['plan'] = name
    purchase['quantity'] = 1

    request.session['purchase'] = purchase

    if not stripe_public_key:
        print(request, 'No stripe public key present.')

    context = {
        'order': order,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }
    print(request.session['purchase'])
    return render(request, 'checkout/checkout-order.html', context=context)


def checkout_complete(request):
    """A view that renders the order payment page"""

    return render(request, 'checkout/checkout-complete.html')
