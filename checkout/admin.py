from django.contrib import admin
from .models import Order


class OrderAdmin(admin.ModelAdmin):

    readonly_fields = ('order_id', 'date',
                       'qty', 'price')

    fields = ('order_id', 'date', 'plan_name', 'plan_type',
              'plan_friendly_name', 'qty', 'price', 'first_name',
              'last_name', 'email', 'password', 'phone_number',
              'postcode', 'billing_address', 'county')

    list_display = ('order_id', 'date', 'first_name',
                    'last_name', 'plan_name', 'qty',
                    'price')

    ordering = ('-date',)


admin.site.register(Order, OrderAdmin)
