from django.shortcuts import render, redirect, reverse
from plans.models import Plan
from .models import Order


def checkout_order(request, name):
    """A view that renders the order summary page"""

    order = Plan.objects.get(name=name)

    context = {
        'order': order,
        'stripe_public_key': 'pk_test_51J2w92Gvf3CD91ZSzCMQT2SmD2pJVGAOJoYcImcZbhKny0SbHqH8jVmghzMQObtdd8nRKzqju6LCc0UjN1aFimT700YPnEvt3Q',
        'client_secret': 'test client secret',

    }

    return render(request, 'checkout/checkout-order.html', context=context)


def checkout_payment(request):
    """A view that renders the order payment page"""

    return render(request, 'checkout/checkout-payment.html')
