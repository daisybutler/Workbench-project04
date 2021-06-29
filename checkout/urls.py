from django.urls import path
from . import views

urlpatterns = [
    path('<name>', views.checkout_order, name='checkout_order'),
    path('checkout_complete/<order_id>', views.checkout_complete, name='checkout_complete'),
]
