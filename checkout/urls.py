from django.urls import path
from . import views

urlpatterns = [
    path('', views.checkout_order, name='checkout_order'),
]
