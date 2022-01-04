from django import forms
from django.contrib.auth import models
from django.forms import fields
from .models import Product

class ProductFrom(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name','category','quantity']
