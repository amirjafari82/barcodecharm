from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from products.models import Product

class Home(View):
    
    def get(self,request):
        products = Product.objects.all()
        return render(request,'home/index.html',{'products':products})
    
    
class AboutMe(View):
    def get(self,request):
        return render(request,'home/aboutme.html')