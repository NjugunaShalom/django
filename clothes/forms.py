from django import forms

from clothes.models import Dress,Shirt

class DressForm(forms.ModelForm):
    class Meta:
        model = Dress
        fields = '__all__'
        widgets = {
            'description': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter the description'}),
            'brand': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter the brand name'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter the price'}),
            'purchase_date': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Enter the purchase date'}),
            'size': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter the size'}),
            'occasion': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter the occasion'}),
        }

class ShirtForm(forms.ModelForm):
    class Meta:
        model = Shirt
        fields = '__all__'
        widgets = {
            'description': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter the description'}),
            'brand': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter the brand name'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter the price'}),
            'purchase_date': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Enter the purchase date'}),
            'size': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter the size'}),
            'occasion': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter the occasion'}),
        }