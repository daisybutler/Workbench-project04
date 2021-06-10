from django.shortcuts import render
from django.shortcuts import render, get_object_or_404


def login(request):
    """A view to display login page."""

    return render(request, 'profiles/login.html')
