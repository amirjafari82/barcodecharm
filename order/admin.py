from django.contrib import admin
from .models import Order, OrderProduct

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['product','ordertracking','user','totalprice','paid']
    search_fields = ['ordertracking','firstname','lastname']
    list_filter = ['paid']
    
@admin.register(OrderProduct)
class OrderProductsAdmin(admin.ModelAdmin):
    list_display = ['product','order','color']