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
from django.template.loader import render_to_string
from django.core.mail import send_mail

from django.contrib import messages
import stripe
import json


def checkout_order(request, name):

    """Purchase a plan securely via Stripe"""

    if request.user.is_superuser:
        messages.error(
            request, 'You are logged in as an administrator. \
             Set up a customer profile to access the checkout process.')
        return redirect(reverse('account_logout'))

    else:
        # Checkout variables
        stripe_public_key = settings.STRIPE_PUBLIC_KEY
        stripe_secret_key = settings.STRIPE_SECRET_KEY
        order = Plan.objects.get(name=name)
        locations = Locations.objects.all()

        # If a user clicks pay
        if request.method == 'POST':
            purchase = request.session.get('purchase', {})
            order = Plan.objects.get(name=name)

            # Gather data inputed by user in checkout form
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
                'password': '******',
                'phone_number': request.POST['phone_number'],
                'county': request.POST['county'],
                'postcode': request.POST['postcode'],
                'billing_address': request.POST['billing_address'],
            }

            user_password = request.POST['password']

            # Redirect to login page if email is
            # already associated with an account
            try:
                User.objects.get(email=form_data['email'])
                messages.error(request, 'This email address is already associated \
                     with a Workbench account. Please log in.')
                return redirect(reverse('account_login'))

            # If email is not found, continue with checkout process
            except User.DoesNotExist:
                pass

            # Populate instance of CheckoutForm form with data
            checkout_form = CheckoutForm(form_data)
            if checkout_form.is_valid():
                completed_order = checkout_form.save(commit=False)
                pid = request.POST.get('client_secret').split('_secret')[0]
                completed_order.stripe_pid = pid
                completed_order.original_purchase = json.dumps(purchase)
                completed_order.save()

                # Check if the user already has a user profile
                if request.user.is_authenticated:
                    new_user = request.user.username
                    pass

                # Else create the user a user profile
                else:
                    # Create a user profile in the database
                    username = form_data['first_name'] \
                        + form_data['last_name'] \
                        + (form_data['phone_number'])[-4:]
                    email = form_data['email']
                    password = user_password

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

                try:
                    # Send email confirmation
                    context = {
                        'email': user.email,
                        'user': new_user,
                        'activate_url': 'accounts/login/',
                        'protocol': 'https' if request.is_secure() else "http",
                        'domain': request.get_host(),
                    }

                    text = render_to_string('../templates/allauth/account/email/email_confirmation_message.txt', context)
                    send_mail(
                        'Welcome to Workbench!',
                        message=text,
                        recipient_list=[user.email],
                        auth_user=settings.EMAIL_HOST_USER,
                        auth_password=settings.EMAIL_HOST_PASSWORD,
                        from_email=settings.DEFAULT_FROM_EMAIL,
                        fail_silently=False,
                    )

                except Exception:
                    pass

                # Redirect user to confirmation page
                return redirect(
                    reverse(
                        'checkout_complete', args=[completed_order.order_id])
                    )

            # If form is flagged as invalid
            else:
                messages.error(request, 'There was an error with your form. \
                    Please double check your information.')

        # Load blank checkout page for user to complete checkout form
        else:
            # Grab context from session
            purchase = request.session.get('purchase', {})
            purchase['plan'] = name
            # purchase['quantity'] = 1
            purchase['price'] = int(order.price)
            purchase['price_id'] = order.price_id

            request.session['purchase'] = purchase

            if not purchase:
                messages.error(
                    request,
                    "Whoops, something went wrong. Please reselect a plan."
                )
                return redirect(reverse('all_plans'))

            # Create Stripe payment intent
            total = purchase['price']
            # qty = purchase['quantity']
            stripe.api_key = stripe_secret_key
            intent = stripe.PaymentIntent.create(
                amount=round(total * 100),
                currency=settings.STRIPE_CURRENCY,
            )

            # If user already as an account, try to grab
            # billing details from previous checkout
            if request.user.is_authenticated:
                try:
                    profile = UserProfile.objects.get(user=request.user)
                    checkout_form = CheckoutForm(initial={
                        'first_name': profile.user.first_name,
                        'last_name': profile.user.last_name,
                        'phone_number': profile.default_phone_number,
                        'billing_address': profile.default_billing_address,
                        'postcode': profile.default_postcode,
                        'county': profile.default_county,
                        'email': profile.user.email,
                    })

                    checkout_form.fields['email'].widget.attrs['readonly'] = True
                    checkout_form.fields['password'].widget.attrs['readonly'] = True

                # Render empty checkout form if user cannot be found
                except UserProfile.DoesNotExist:
                    checkout_form = CheckoutForm()

            # Render empty checkout form if user not logged in
            else:
                checkout_form = CheckoutForm()

            # Variables for newly created order
            order = Plan.objects.get(name=name)

            # Stripe key reminder
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

            return render(
                request, 'checkout/checkout-order.html', context=context
            )


def checkout_complete(request, order_id):

    """Renders the order complete page"""

    order = get_object_or_404(Order, order_id=order_id)

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
            'profile': profile,
        }

        if 'purchase' in request.session:
            del request.session['purchase']

        return render(
                request, 'checkout/checkout-complete.html', context=context
            )

