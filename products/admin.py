from django.contrib import admin
from .models import Comment, Product, ProductImage

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title','price','number','created')
    prepopulated_fields = {'slug': ('title',)}
    
@admin.register(ProductImage)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('product',)
    
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user','product','created','approved')
    raw_id_fields = ('user','product')