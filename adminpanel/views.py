import json
import os
from django.core import serializers
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from products.models import Comment, Product, ProductImage
from weblog.models import Article
from order.models import Order, OrderProduct
from contactus.models import Contact
from .models import DiscountCode
from .forms import AddProductForm, AddProductImageForm, UpdateProductForm, AddArticleForm, UpdateArticleForm, AddDiscountForm, ChangeOrderStatusForm, ChangeContactSituation, OrderSearchForm, ApproveCommentForm
from django.utils.text import slugify
from django.views.generic import CreateView, UpdateView, DeleteView

class AdminView(LoginRequiredMixin,View):
    discount_form = AddDiscountForm
    contact_form = ChangeContactSituation
    
    def get(self,request):
        if self.request.user.username == '09398708391':
            products = Product.objects.all()
            articles = Article.objects.all()
            discounts = DiscountCode.objects.all()
            contacts = Contact.objects.all()
            return render(request,'adminpanel/admin.html',{'products':products,'articles':articles,'discount_form':self.discount_form,'discounts':discounts,'contacts':contacts,'contact_form':self.contact_form})
        else:
            return redirect('home:home')
        
    def post(self,request):
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            contact_id = request.POST.get('contact_id')
            situation = request.POST.get('situation')
            contact = Contact.objects.get(id=contact_id)
            contact.situation = situation
            contact.save()
            return JsonResponse({'status':'ok','id':contact_id,'situation':situation})
        form = self.discount_form(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'اضافه شد','success')
            return redirect('adminpanel:adminpanel')
    
class AddProductView(LoginRequiredMixin,View):
    product_form = AddProductForm
    image_form = AddProductImageForm
        
    def get(self,request):
        if self.request.user.username == '09398708391':
            return render(request,'adminpanel/addproduct.html',{'product_form':self.product_form,'image_form':self.image_form})
        else:
            return redirect('home:home')
        
    def post(self,request):
        form = self.product_form(request.POST,request.FILES)
        files = self.request.FILES.getlist('image')
        if form.is_valid():
            new_product = form.save(commit=False)
            new_product.slug = slugify(form.cleaned_data['title'],allow_unicode=True)
            new_product.save()
            for image in files:
                color = image.name.split(".")[0]
                if 'green' in color:
                    color = 'green'
                if 'blue' in color:
                    color = 'blue'
                if 'red' in color:
                    color = 'red'
                if 'black' in color:
                    color = 'black'
                if 'brown' in color:
                    color = 'brown'
                if 'crimson' in color:
                    color = 'crimson'
                ProductImage.objects.create(product=new_product,image=image,color=color)
                    
            messages.success(request,'محصول با موفقیت ساخته شد','success')
            return redirect('adminpanel:adminpanel')
        else:
            print(form.errors)
            return redirect('adminpanel:adminpanel')
        
class EditProdcut(LoginRequiredMixin,UpdateView):
    
    def dispatch(self, request, *args, **kwargs):
        if self.request.user.username != '09398708391':
            return redirect('home:home')
        return super().dispatch(request, *args, **kwargs)
    
    model = Product
    success_url = reverse_lazy('adminpanel:adminpanel')
    template_name = 'adminpanel/updateproduct.html'
    form_class = UpdateProductForm
    
    def form_valid(self, form):
        new_prod = form.save(commit=False)
        new_prod.slug = slugify(form.cleaned_data['title'],allow_unicode=True)
        new_prod.save()
        messages.success(self.request,'ویرایش شد','success')
        return super().form_valid(form)
    
    
class DeleteProduct(LoginRequiredMixin,View):
    
    def get(self,request,prod_id):
        if self.request.user.username == '09398708391':
            product = Product.objects.get(id=prod_id)
            productimages = ProductImage.objects.filter(product=product)
            if len(product.peresentimage) > 0:
                os.remove(product.peresentimage.path)
                for image in productimages:  
                    os.remove(image.image.path)
            product.delete()
            productimages.delete()
            messages.success(request,'با موفقیت حذف شد','success')
            return redirect('adminpanel:adminpanel')
        else:
            return redirect('home:home')
        
class AddArticle(LoginRequiredMixin,CreateView):
    
    def dispatch(self, request, *args, **kwargs):
        if self.request.user.username != '09398708391':
            return redirect('home:home')
        return super().dispatch(request, *args, **kwargs)
    
    model = Article
    form_class = AddArticleForm
    success_url = reverse_lazy('adminpanel:adminpanel')
    template_name = 'adminpanel/addarticle.html'
    
    def form_valid(self, form):
        new_arti = form.save(commit=False)
        new_arti.slug = slugify(form.cleaned_data['title'],allow_unicode=True)
        new_arti.save()
        messages.success(self.request,'مقاله با موفقیت ساخته شد','success')
        return super().form_valid(form)
    
class EditArticle(LoginRequiredMixin,UpdateView):
    
    def dispatch(self, request, *args, **kwargs):
        if self.request.user.username != '09398708391':
            return redirect('home:home')
        return super().dispatch(request, *args, **kwargs)
    
    model = Article
    success_url = reverse_lazy('adminpanel:adminpanel')
    template_name = 'adminpanel/updatearticle.html'
    form_class = UpdateArticleForm
    
    def form_valid(self, form):
        new_prod = form.save(commit=False)
        new_prod.slug = slugify(form.cleaned_data['title'],allow_unicode=True)
        new_prod.save()
        messages.success(self.request,'ویرایش شد','success')
        return super().form_valid(form)
    
class DeleteArticle(LoginRequiredMixin,View):
    
    def get(self,request,arti_id):
        if self.request.user.username == '09398708391':
            article = Article.objects.get(id=arti_id)
            if len(article.image) > 0:
                os.remove(article.image.path)
            article.delete()
            messages.success(request,'با موفقیت حذف شد','success')
            return redirect('adminpanel:adminpanel')
        else:
            return redirect('home:home')
        
class DeleteDiscount(LoginRequiredMixin,View):
    
    def get(self,request,dis_id):
        if self.request.user.username == '09398708391':
            discount = DiscountCode.objects.get(id=dis_id)
            discount.delete()
            messages.success(request,'با موفقیت حذف شد','success')
            return redirect('adminpanel:adminpanel')
        else:
            return redirect('home:home')
        
class AdminOrders(LoginRequiredMixin,View):
    form_class = OrderSearchForm
    
    def get(self,request):
        if self.request.user.username == '09398708391':
            orders = Order.objects.filter(paid=True).order_by("-id")
            products = OrderProduct.objects.all()
            income = 0
            for order in orders:
                income += int(order.totalprice.replace(",",""))
            if request.GET.get('search'):
                orders = orders.filter(ordertracking__contains=request.GET['search'])
            return render(request,'adminpanel/orders.html',{'products':products,'orders':orders,'income':income,'form':self.form_class})
        else:
            return redirect('home:home')
        
class AdminOrderDetail(LoginRequiredMixin,View):
    form_class = ChangeOrderStatusForm
    
    def get(self,request,order_id):
        order = Order.objects.get(id=order_id)
        form = self.form_class(instance=order)
        products = order.order.all()
        if self.request.user.username == '09398708391':
            order = Order.objects.get(id=order_id)
            colorlist = {}
            for product in products:
                new_list = product.color.replace("'",'').strip('][').split(', ')
                colorlist[product.id] = {'color': new_list}
            return render(request,'adminpanel/orderdetail.html',{'colors':colorlist,'order':order,'form':form})
        else:
            return redirect('home:home')
        
    def post(self,request,order_id):
        order = Order.objects.get(id=order_id)
        form = self.form_class(request.POST,instance=order)
        if form.is_valid():
            form.save()
            messages.success(request,'ثبت شد','success')
            return redirect('adminpanel:adminpanel')
        
class DeleteUserComment(LoginRequiredMixin,View):

    def get(self,request,comment_id):
        comment = get_object_or_404(Comment,id=comment_id)
        if request.user.username == '09398708391':
            comment.delete()
            messages.success(request,'کامنت حذف شد','success')
            return redirect('products:detail',comment.product.slug)
        else:
            return redirect('home:home')
        
class CommentsAdminView(LoginRequiredMixin,View):
    form_class = ApproveCommentForm
    
    def get(self,request):
        if request.user.username == '09398708391':
            comments = Comment.objects.all()
            return render(request,'adminpanel/comments.html',{'comments':comments,'approve_form':self.form_class})
        else:
            return redirect('home:home')
    
    def post(self,request):
        if request.user.username == '09398708391':
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                comment_id = request.POST.get('comment_id')
                approved = request.POST.get('approved')
                if approved == 'true':
                    approved = True
                if approved == 'false':
                    approved = False
                comment = Comment.objects.get(id=comment_id)
                comment.approved = approved
                comment.save()
                return JsonResponse({'status':'ok'})