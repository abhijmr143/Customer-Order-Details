from django.db import models

# Create your models here.

class CustomerOrderDetails(models.Model):
    customer = models.CharField(max_length=200)
    products = models.CharField(max_length=200)
    order_sales = models.IntegerField(default=0)
    order_units = models.IntegerField(default=0)

    def __str__(self):
        return self.customer

