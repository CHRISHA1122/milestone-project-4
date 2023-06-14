from django import forms
from .models import CustomizableProduct


class CustomizableProductForm(forms.ModelForm):
    class Meta:
        model = CustomizableProduct
        fields = ['main_color', 'wording_color', 'writing']
