from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.contrib import messages
from django.utils.encoding import uri_to_iri
from .models import Product, Comment, ProductImage
from .forms import CommentForm
from django.contrib.auth.mixins import LoginRequiredMixin


class ProductList(View):
    
    def get(self,request):
        products = Product.objects.all()
        productimages = ProductImage.objects.all()
        return render(request,'products/index.html',{'products':products,'productimages':productimages})
    
class ProductDetail(View):
    
    def get(self,request,slug):
        product = get_object_or_404(Product,slug=uri_to_iri(slug))
        comments = Comment.objects.filter(product=product,approved=True)
        total_score = 0
        numbers = 0
        for comment in comments:
            total_score += comment.score
            numbers += 1
        if numbers == 0:
            avgscorecomments = 0
        else:
            avgscorecomments = total_score / numbers
            avgscorecomments = round(avgscorecomments,1)
        productimage = ProductImage.objects.filter(product=product)
        colorslist = product.colors.strip('][').split(', ')
        return render(request,'products/detail.html',{'product':product,'comments':comments,'productimage':productimage,'colors':colorslist,'avg':avgscorecomments})
    
    def post(self,request,slug):
        product = Product.objects.get(slug=slug)
        score = request.POST.get('val')
        body = request.POST.get('body')
        user = request.user
        if body == None:
            return redirect('products:detail',slug)
        new_comment = Comment.objects.create(user=user,score=score,body=body,product=product)
        new_comment.save()
        messages.success(request,'کامنت شما با موفقیت ثبت شد و در انتظار تایید است. باتشکر','success')
        return JsonResponse({'status':'ok'})
    
class DeleteUserComment(LoginRequiredMixin,View):

    def get(self,request,comment_id):
        comment = get_object_or_404(Comment,id=comment_id)
        if request.user.id == comment.user.id:
            comment.delete()
            messages.success(request,'کامنت شما با موفقیت حذف شد','success')
            return redirect('products:detail',comment.product.slug)
        else:
            return redirect('home:home')