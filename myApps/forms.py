from django import forms
from .models import CustomerOrderDetails

class CustomerOrderDetailsForm(forms.ModelForm):
    class Meta:
        model = CustomerOrderDetails
        fields = '__all__'
        