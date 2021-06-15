from django.shortcuts import render
from plans.models import Plan
import datetime


def checkout_order(request, name):
    """A view that renders the order summary page"""

    order = Plan.objects.get(name=name)

    context = {
        'order': order,
    }

    return render(request, 'checkout/checkout-order.html', context=context)


def checkout_payment(request):
    """A view that renders the order payment page"""

    return render(request, 'checkout/checkout-payment.html')
