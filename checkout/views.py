from django.shortcuts import render
from plans.models import Plan


def checkout_order(request, name):
    """A view that renders the order summary page"""

    order = Plan.objects.get(name=name)

    context = {
        'order': order,
    }

    return render(request, 'checkout/checkout-order.html', context=context)
