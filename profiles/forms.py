from django import forms


class UserLogin(forms.Form):
    email = forms.CharField(label='email', max_length=40),
    password = forms.CharField(label='password', max_length=40),
