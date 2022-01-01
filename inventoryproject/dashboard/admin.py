from django.contrib import admin
from django.contrib.admin.filters import ListFilter
from .models import *
from django.contrib.auth.models import Group

admin.site.site_header = 'TongInventory Dashboard'

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','category','quantity')
    list_filter = ['category']

class OrderAdmin(admin.ModelAdmin):
    pass

# Register your models here.
admin.site.register(Product,ProductAdmin)
admin.site.register(Order,OrderAdmin)
# admin.site.unregister(Group)