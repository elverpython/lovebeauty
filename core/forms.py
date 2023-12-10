from django import forms
from .models import Brands, Clients


class BrandEditForm(forms.ModelForm):
    class Meta:
        model = Brands
        fields = [
            'name',
            'description',
            'workers',

        ]

class BrandAddForm(forms.ModelForm):
    class Meta:
        model = Brands
        fields = [
            'name',
            'description',
            'contacts',
            'workers',

        ]


class ClientEditForm(forms.ModelForm):
    class Meta:
        model = Clients
        fields = [
            'name',
            'description',
            'address',
            'contacts',
            'workers',
            'brand',

        ]

class ClientAddForm(forms.ModelForm):
    class Meta:
        model = Clients
        fields = [
            'name',
            'description',
            'address',
            'contacts',
            'workers',
            'brand',

        ]