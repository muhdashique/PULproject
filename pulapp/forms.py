from django import forms


from django.contrib import admin
from .models import FuelRate

from django import forms
from .models import FuelRate  # Ensure FuelRate model exists in models.py

class FuelRateForm(forms.ModelForm):
    class Meta:
        model = FuelRate
        fields = ['country', 'fuel_rate']






