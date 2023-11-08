from django.contrib import admin
from .models import Contact

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('title','firstname','lastname','phonenumber','situation')
    list_filter = ['situation']