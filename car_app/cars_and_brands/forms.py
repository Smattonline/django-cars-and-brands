from django import forms
from .models import Brand, Car

class BrandForm(forms.ModelForm):
    class Meta:
        model = Brand
        fields = ['name', 'company']

class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['brand', 'year', 'make', 'model', 'price', 'color']