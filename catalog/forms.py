from django import forms
from django.urls import reverse_lazy

from catalog.models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        # fields = ('name', 'category',)
        # exclude = ('image',)
        # success_url = reverse_lazy('catalog:index')
