from django import forms
from django.forms import ModelForm
from olx.models import Product


class AddProduct(forms.ModelForm):
    class Meta:
        model = Product
        exclude = ['category', 'seller', 'is_sold', 'buyer', 'sold_on', 'posted_on','views']
        widgets = {
            'name' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}),
            'price' : forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Price'}),
            'image' : forms.FileInput(attrs={'class': 'form-control', 'placeholder': 'Upload Picture'}),
            'description' : forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Description of Product'})
        }
