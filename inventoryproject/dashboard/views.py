from django import forms
from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Product, Order
from django.contrib.auth.decorators import login_required
from .forms import ProductFrom,OrderForm
from django.contrib.auth.models import User
# Create your views here.

@login_required
def index(request):
    orders = Order.objects.all()
    orders_count = orders.count()

    products = Product.objects.all()
    products_count = products.count()

    workers = User.objects.all()
    workers_count = workers.count()

    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            product_name = form.cleaned_data.get('product')
            order_quantity = form.cleaned_data.get('order_quantity')
            if product_name.quantity == 0:
                messages.info(request, f'{product_name.name} out of stock')
                return redirect('dashboard-index')

            if int(product_name.quantity) <  int(order_quantity):
                messages.info(request, f'{product_name.name} quantity is exceeded')
                return redirect('dashboard-index')
            
            final_quantity = int(product_name.quantity) - int(order_quantity)
            product_query = Product.objects.get(name=product_name.name)
            product_query.quantity = final_quantity
            product_query.save()

            instance = form.save(commit=False)
            instance.staff = request.user
            instance.save()
            return redirect('dashboard-index')
    else:
        form = OrderForm()
    context = {
        'orders':orders,
        'form':form,
        'products':products,
        'workers_count':workers_count,
        'orders_count':orders_count,
        'products_count':products_count,
    }
    return render(request, 'dashboard/index.html',context)

@login_required
def staff(request):
    orders = Order.objects.all()
    orders_count = orders.count()

    products = Product.objects.all()
    products_count = products.count()

    workers = User.objects.all()
    workers_count = workers.count()
    context = {
        'workers':workers,
        'workers_count':workers_count,
        'orders_count':orders_count,
        'products_count':products_count,
    }
    return render(request, 'dashboard/staff.html',context)

def staff_detail(request, pk):
    workers = User.objects.get(id=pk)
    context = {
        'workers':workers,
    }
    return render(request,'dashboard/staff_detail.html',context)

@login_required
def product(request):
    items = Product.objects.all()
    orders = Order.objects.all()
    orders_count = orders.count()

    products = Product.objects.all()
    products_count = products.count()

    workers = User.objects.all()
    workers_count = workers.count()
    if request.method == 'POST':
        form = ProductFrom(request.POST)
        if form.is_valid():
            form.save()
            product_name = form.cleaned_data.get('name') # เป็นการ get data name ใน table product
            messages.success(request, f'{product_name} has been added')
            return redirect('dashboard-product') # ถ้าใส่ action ใน form ของ html ไม่จำเป็นต้องใส่ return ก็ได้
    else:
        form = ProductFrom()
    context = {
        'items':items,
        'form':form,
        'workers_count':workers_count,
        'orders_count':orders_count,
        'products_count':products_count,
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
    orders = Order.objects.all()
    orders = Order.objects.all()
    orders_count = orders.count()

    products = Product.objects.all()
    products_count = products.count()

    workers = User.objects.all()
    workers_count = workers.count()
    context = {
        'orders':orders,
        'workers_count':workers_count,
        'orders_count':orders_count,
        'products_count':products_count,
    }
    return render(request, 'dashboard/order.html',context)