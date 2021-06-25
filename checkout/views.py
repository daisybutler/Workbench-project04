from django.shortcuts import render, redirect, reverse
from django.conf import settings

from plans.models import Plan
from .forms import CheckoutForm
from .models import Order

from django.contrib import messages
from checkout.contexts import purchase_contents
import stripe


def checkout_order(request, name):

    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        purchase = request.session.get('purchase', {})
        order = Plan.objects.get(name=name)

        form_data = {
            'plan_name': name,
            'plan_type': 'plan type',
            'plan_friendly_name': 'friendly name',
            'qty': 1,
            'price': 'price',
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
            new_order = checkout_form.save()
            return redirect(reverse('checkout_complete'))
        
        else:
            messages.error(request, 'There was an error with your form. \
                Please double check your information.')

    else:
        purchase = request.session.get('purchase', {})
        purchase['plan'] = name
        purchase['quantity'] = 1

        request.session['purchase'] = purchase

        print(purchase)
        if not purchase:
            messages.error(request, "Whoops, something went wrong. Please select a plan.")
            return redirect(reverse('all_plans'))

        current_purchase = purchase_contents(request)
        total = 50
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=total,
            currency=settings.STRIPE_CURRENCY,
        )

        order = Plan.objects.get(name=name)
        checkout_form = CheckoutForm()

        if not stripe_public_key:
            messages.warning(request, 'Stripe public key is missing. \
                Did you forget to set it in your environment?')

        template = 'checkout/checkout-order.html'
        context = {
            'order': order,
            'checkout_form': checkout_form,
            'stripe_public_key': stripe_public_key,
            'client_secret': intent.client_secret,
        }

        return render(request, 'checkout/checkout-order.html', context=context)


def checkout_complete(request):
    """A view that renders the order payment page"""

    if 'purchase' in request.session:
        del request.session['purchase'] 

    return render(request, 'checkout/checkout-complete.html')
