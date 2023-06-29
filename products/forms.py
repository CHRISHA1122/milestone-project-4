from django import forms
from .widgets import CustomClearableFileInput
from .models import Product, Category, Color


class ProductForm(forms.ModelForm):

    main_color = forms.ModelChoiceField(queryset=Color.objects.all(), widget=forms.Select, required=False)
    wording_color = forms.ModelChoiceField(queryset=Color.objects.all(), widget=forms.Select, required=False)
    writing = forms.CharField(max_length=100, required=False)

    class Meta:
        model = Product
        exclude = ['colors']
        widgets = {
            'image': CustomClearableFileInput,
        }

    image = forms.ImageField(label='Image', required=False, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'
