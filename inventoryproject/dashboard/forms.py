from django import forms
from django.contrib.auth import models
from django.forms import fields
from .models import Order, Product

class ProductFrom(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name','category','quantity']

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['product', 'order_quantity']
