from django import forms
from .models import GalleryImage, FuelRate






class FuelRateForm(forms.ModelForm):
    class Meta:
        model = FuelRate
        fields = ['country', 'fuel_rate']






class GalleryImageForm(forms.ModelForm):
    class Meta:
        model = GalleryImage
        fields = ['title', 'description', 'image']

