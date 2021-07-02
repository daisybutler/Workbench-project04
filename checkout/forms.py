from django import forms
from .models import Order


class CheckoutForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('plan_name', 'plan_friendly_name', 'plan_type',
                  'location', 'price', 'first_name',
                  'last_name', 'email', 'password',
                  'phone_number', 'billing_address', 'postcode',
                  'county')

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'first_name': 'Full Name*',
            'last_name': 'Last Name*',
            'email': 'Email Address*',
            'password': 'Password*',
            'phone_number': 'Phone Number*',
            'billing_address': 'Billing Address*',
            'postcode': 'Postcode*',
            'county': 'County*',
        }
