from django import forms


from django.contrib import admin
from .models import FuelRate,GalleryImage

from django import forms
from .models import FuelRate  # Ensure FuelRate model exists in models.py

class FuelRateForm(forms.ModelForm):
    class Meta:
        model = FuelRate
        fields = ['country', 'fuel_rate']





from django import forms
from .models import GalleryImage

class GalleryImageForm(forms.ModelForm):
    class Meta:
        model = GalleryImage
        fields = ['title', 'description', 'image']

