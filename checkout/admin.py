from django.contrib import admin
from .models import Order


class OrderAdmin(admin.ModelAdmin):

    readonly_fields = ('order_id', 'date', 'price')

    fields = ('order_id', 'user_profile', 'date', 'plan_name', 'plan_type',
              'plan_friendly_name', 'location', 'price', 'first_name',
              'last_name', 'email', 'password', 'phone_number',
              'postcode', 'billing_address', 'county', 'stripe_pid')

    list_display = ('order_id', 'date', 'first_name',
                    'last_name', 'plan_name', 'location',
                    'price', 'stripe_pid')

    ordering = ('-date',)


admin.site.register(Order, OrderAdmin)
