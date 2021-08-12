from django.contrib import admin
from .models import CustomerOrderDetails

# Register your models here.


@admin.register(CustomerOrderDetails)
class CustomerOrderDetailsAdmin(admin.ModelAdmin):
    list_display = [
        'id', 
        'customer',
        'products',
        'order_sales',
        'order_units',
    ]