from django import forms
from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Product
from django.contrib.auth.decorators import login_required
from .forms import ProductFrom
# Create your views here.

@login_required
def index(request):
    return render(request, 'dashboard/index.html')

@login_required
def staff(request):
    return render(request, 'dashboard/staff.html')

@login_required
def product(request):
    items = Product.objects.all()

    if request.method == 'POST':
        form = ProductFrom(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard-product') # ถ้าใส่ action ใน form ของ html ไม่จำเป็นต้องใส่ return ก็ได้
    else:
        form = ProductFrom()
    context = {
        'items':items,
        'form':form,
    }
    return render(request, 'dashboard/product.html',context)

def product_delete(request, pk):
    item = Product.objects.get(id=pk)
    if request.method=='POST':
        item.delete()
        return redirect('dashboard-product')
    return render(request, 'dashboard/product_delete.html')

def product_update(request, pk):
    item = Product.objects.get(id=pk)
    if request.method=='POST':
        form = ProductFrom(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('dashboard-product')
    else:
        form = ProductFrom(instance=item)

    context = {
        'form':form
    }
    return render(request, 'dashboard/product_update.html',context)

@login_required
def order(request):
    return render(request, 'dashboard/order.html')