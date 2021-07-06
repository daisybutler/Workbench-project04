from django import forms
from .models import UserProfile


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and set autofocus of
        first field.
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'default_first_name': 'Full Name',
            'default_last_name': 'Last Name',
            'default_email': 'Email Address',
            'default_phone_number': 'Phone Number',
            'default_billing_address': 'Billing Address',
            'default_postcode': 'Postcode',
            'default_county': 'County',
        }

        self.fields['default_phone_number'].widget.attrs['autofocus'] = True
