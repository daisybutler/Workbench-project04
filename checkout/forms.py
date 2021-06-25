from django import forms
from .models import Order


class CheckoutForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('fname', 'lname', 'email', 'password', 'phone_number',
                  'billing_address', 'postcode', 'county')

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'fname': 'Full Name*',
            'lname': 'Last Name*',
            'email': 'Email Address*',
            'password': 'Password*',
            'phone_number': 'Phone Number*',
            'billing_address': 'Billing Address*',
            'postcode': 'Postcode*',
            'county': 'County*',
        }
