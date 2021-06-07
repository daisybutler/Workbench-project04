from django.shortcuts import render

def checkout_order(request):
    """A view that renders the order summary page"""
    
    return render(request, 'checkout/checkout-order.html')

