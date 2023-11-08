from django.contrib import admin
from .models import DiscountCode, AdminModel

@admin.register(DiscountCode)
class DiscountCodeAdmin(admin.ModelAdmin):
    list_display = ['code','discount','created']
    
@admin.register(AdminModel)
class AdminModelAdmin(admin.ModelAdmin):
    list_display = ['buy',]