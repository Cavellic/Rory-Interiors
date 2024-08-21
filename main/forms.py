from django import forms
from .models import *


class TestimonyForm(forms.ModelForm):
    class Meta:
        model = Testimonial
        fields = ('first_name', 'last_name', 'review', 'image')
        
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'review': forms.TextInput(attrs={'class': 'form-control'})
        }


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('product_type','image')
        
        widgets = {
            'product_type': forms.Select(attrs={'class': 'form-control'}),
            
        }

        
        
class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ('client', 'item', 'quantity', 'item_pic', 'fabric', 'description')
        
        widgets = {
            'client': forms.Select(attrs={'class': 'form-control'}),
            'item': forms.TextInput(attrs={'class': 'form-control'}),
            'quantity': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'quantity': forms.TextInput(attrs={'class': 'form-control'})
        }
