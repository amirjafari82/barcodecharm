import json
from django.http import JsonResponse
from django.views import View
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from products.models import Product, ProductImage
from adminpanel.models import AdminModel
from .forms import DiscountForm
from django.contrib.auth.models import User
from order.models import Order, OrderProduct
from .cart import Cart


class CartView(LoginRequiredMixin,View):
    discount_form = DiscountForm
    
    def get(self,request,user_id):
        if request.user.id == user_id:
            cart = Cart(request)
            if request.session['cart'] == {}:
                messages.error(request,'سبد خرید شما خالی است','danger')
                return redirect('products:products')
            else:
                for item in cart:
                    print(item)
                prod_id = list(request.session['cart'].keys())
                user_cart = Product.objects.filter(id__in=prod_id)
                productimages = ProductImage.objects.filter(product__in=user_cart)
            # total = 0
            # for product in user_cart:
            #     price = product.price.replace(',','')
            #     if product.discount == False:
            #         total += int(price)
            #     else:
            #         offprice = product.offprice.replace(',','')
            #         total += int(offprice)
            # total = f"{total:,d}"
            return render(request,'cart/index.html',{'cart':cart,'usercart':user_cart,'productimages':productimages,'discount_form':self.discount_form})
        else:
            return redirect('home:home')
                    
class AddToCart(View):
    
    def post(self,request,prod_id):
        cart = Cart(request)
        buy = AdminModel.objects.get(id=1)
        data = json.loads(self.request.body.decode("utf-8"))
        color = data.get('choosedcolor')
        product_id = data.get('prod_id')
        product = get_object_or_404(Product,id=product_id)
        if request.user.is_authenticated:
            user = User.objects.get(id=request.user.id)
            order = Order.objects.filter(user=user,postdelivered=False)
            if order.exists():
                return JsonResponse({'status':'Active Order'})
        if not self.request.user.is_authenticated:
            return JsonResponse({'status':'NotLoggedIn'})
        if color == None:
            return JsonResponse({'status':'null'})
        if buy.buy == False:
            return JsonResponse({'status':'False Buy'})
        else:
            for item in cart:
                if color in item['color']:
                    return JsonResponse({'status':'Common Color'})
            cart.add(product,color)
        return JsonResponse({'status':'success','color':color,'user_id':request.user.id})
    
class RemoveItem(LoginRequiredMixin,View):
    
    def get(self,request,prod_id):
        cart = Cart(request)
        product = get_object_or_404(Product,id=prod_id)
        order_product = OrderProduct.objects.filter(product=product)
        if order_product.exists():
            order_product.delete()
        cart.remove(product)
        messages.success(request,'با موفقیت حذف شد','success')
        return redirect('cart:cart',request.user.id)