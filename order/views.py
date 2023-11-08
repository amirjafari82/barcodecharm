from django.http import HttpResponse, JsonResponse
from django.views import View
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from products.models import Product, ProductImage
from adminpanel.models import AdminModel, DiscountCode
from django.contrib.auth.models import User
from .models import Order, OrderProduct
from .forms import DiscountForm, OrderForm
import random, requests, json
from django.conf import settings
from cart.cart import Cart

class OrderView(LoginRequiredMixin,View):
    discount_form = DiscountForm
    order_form = OrderForm
    
    def get(self,request,user_id):
        if request.user.id == user_id:
            cart = Cart(request)
            if request.session['cart'] != {}:
                buy = AdminModel.objects.get(id=1)
                product_id = list(request.session['cart'].keys())
                products = Product.objects.filter(id__in=product_id)
                productimages = ProductImage.objects.filter(product__in=products)
                user = User.objects.get(id=user_id)
                order = Order.objects.filter(user=user,paid=False)
                order_products = OrderProduct.objects.filter(order__in=order)
                total = 0
                product = Product.objects.get(id=product_id[0])
                for product in products:
                    price = product.price.replace(',','')
                if product.discount == False:
                    total += int(price)
                else:
                    offprice = product.offprice.replace(',','')
                    total += int(offprice)
                total = f"{total:,d}"
                order_ins = None
                if order.exists():
                    print(order_products.exists())
                    if order_products.exists():
                        order_ins = Order.objects.get(user=user,paid=False)
                    else:
                        for item in cart:
                            product = Product.objects.get(id=item['product_id'])
                            order_ins = Order.objects.get(user=user,paid=False)
                            OrderProduct.objects.create(product=product,order=order_ins,color=item['color'])
                else:
                    Order.objects.create(user=user,totalprice=cart.get_total_price(),product=product)
                    for item in cart:
                            product = Product.objects.get(id=item['product_id'])
                            order_ins = Order.objects.get(user=user,paid=False)
                            OrderProduct.objects.create(product=product,order=order_ins,color=item['color'])
                if buy.buy == False:
                    messages.error(request,'در حال حاضر امکان سفارش محصول وجود ندارد','danger')
                    return redirect('products:products')
                print(order_ins)
                return render(request,'order/index.html',{'order':order_ins,'cart':cart,'products':order_products,'productimages':productimages,'total':total,'order_form':self.order_form,'discount_form':self.discount_form})
            else:
                messages.error(request,'شما چیزی برای خرید انتخاب نکردید','danger')
                return redirect('products:products')
        else:
            return redirect('home:home')
        
    def post(self,request,user_id):
        cart = Cart(request)
        pay_form = self.order_form(request.POST)
        discount_form = self.discount_form(request.POST)
        discounts = DiscountCode.objects.all()
        product_id = list(request.session['cart'].keys())
        # product_color = request.session['cart'][0]['color']
        products = Product.objects.filter(id__in=product_id)
        productimages = ProductImage.objects.filter(product__in=products)
        user = User.objects.get(id=user_id)
        order = Order.objects.filter(user=user,paid=False)
        order_products = OrderProduct.objects.filter(order__in=order)
        order_instance = Order.objects.get(paid=False,user=user)
        if discount_form.is_valid():
            user_code = discount_form.cleaned_data['code']
            for code in discounts:
                if code.code == user_code:
                    total = cart.get_total_price()
                    print(total)
                    discount_percent = (100 - code.discount) / 100
                    total = int(total) * discount_percent
                    total = int(total)
                    order_instance.totalprice = total
                    order_instance.save()
                    total = f"{total:,d}"
                    messages.success(request,'کد تخفیف با موفقیت اعمال شد','success')
                    return render(request,'order/index.html',{'order':order_instance,'cart':cart,'products':order_products,'productimages':productimages,'total':total,'order_form':self.order_form,'discount_form':self.discount_form})
                else:
                    messages.error(request,'کد تخفیف اشتباه است','danger')
            return redirect('order:order',request.user.id)
        if pay_form.is_valid():
            randomcode = random.randint(1000,9999)
            test_order = Order.objects.filter(ordertracking=randomcode)
            if test_order.exists():
                randomcode = random.randint(1000,9999)
            order_instance.phonenumber = pay_form.cleaned_data['phonenumber']
            order_instance.city = pay_form.cleaned_data['city']
            order_instance.zipcode = pay_form.cleaned_data['zipcode']
            order_instance.fulladdress = pay_form.cleaned_data['fulladdress']
            order_instance.firstname = pay_form.cleaned_data['firstname']
            order_instance.lastname = pay_form.cleaned_data['lastname']
            order_instance.description = pay_form.cleaned_data['description']
            order_instance.ordertracking = randomcode
            order_instance.save()
            del request.session['cart']
            order_price = order_instance.totalprice.replace(',','')
            if settings.SANDBOX:
                sandbox = 'sandbox'
            else:
                sandbox = 'www'
            ZP_API_REQUEST = f"https://{sandbox}.zarinpal.com/pg/rest/WebGate/PaymentRequest.json"
            ZP_API_STARTPAY = f"https://{sandbox}.zarinpal.com/pg/StartPay/"
            data = {
                "MerchantID": settings.MERCHANT,
                "Amount": order_price,
                "Description": f'خرید بند ساعت',
                "Phone": '',
                "CallbackURL": f'http://127.0.0.1:8000/order/{user_id}/verify/',
            }
            data = json.dumps(data)
            headers = {'content-type': 'application/json', 'content-length': str(len(data)) }
            try:
                response = requests.post(ZP_API_REQUEST, data=data,headers=headers, timeout=10)

                if response.status_code == 200:
                    response = response.json()
                    if response['Status'] == 100:
                        order_instance.authority = str(response['Authority'])
                        order_instance.save()
                        return redirect(ZP_API_STARTPAY+str(response["Authority"]))
                    else:
                        return JsonResponse({'status': False, 'code': str(response['Status'])})
                return response

            except requests.exceptions.Timeout:
                return JsonResponse({'status': False, 'code': 'timeout'})
            except requests.exceptions.ConnectionError:
                return JsonResponse({'status': False, 'code': 'connection error'})
            
def verify(request,user_id):
    user = User.objects.get(id=user_id)
    order_instance = None
    order = Order.objects.filter(user=user,paid=False)
    if not order.exists():
        return render(request,'order/result.html',{'status': 'Paid'})
    for item in order:
        order_instance = item
    order_price = order_instance.totalprice.replace(',','')
    order_authority = order_instance.authority
    data = {
        "MerchantID": settings.MERCHANT,
        "Amount": order_price,
        "Authority": order_authority,
    }
    data = json.dumps(data)
    # set content length by data
    if settings.SANDBOX:
        sandbox = 'sandbox'
    else:
        sandbox = 'www'
    headers = {'content-type': 'application/json', 'content-length': str(len(data)) }
    ZP_API_VERIFY = f"https://{sandbox}.zarinpal.com/pg/rest/WebGate/PaymentVerification.json"
    response = requests.post(ZP_API_VERIFY, data=data,headers=headers)

    if response.status_code == 200:
        response = response.json()
        if response['Status'] == 100:
            order_instance.paid = True
            order_instance.save()
            return render(request,'order/result.html',{'status': True, 'order':order_instance})
        else:
            return render(request,'order/result.html',{'status': False})
    return HttpResponse(response)

        
class CancelOrder(LoginRequiredMixin,View):
    
    def get(self,request,order_id):
        order = get_object_or_404(Order,id=order_id)
        if request.user.id == order.user.id:
            if order.paid == False:
                order.delete()
                cart = Cart(request)
                cart.clear()
                messages.success(request,'سفارش با موفقیت لغو شد','success')
                return redirect('account:profile',request.user.id)
            else:
                return redirect('account:profile',request.user.id)
        else:
            redirect('home:home')
            
class ContinueOrder(LoginRequiredMixin,View):
    
    def get(self,request,order_id):
        order = get_object_or_404(Order,id=order_id)
        if request.user.id == order.user.id:
            cart = Cart(request)
            if order.paid == False:
                if request.session['cart'] == {}:
                    test = order.order.all()
                    for item in test:
                        new_list = item.color.replace("'",'').strip('][').split(', ')
                        for color in new_list:
                            cart.add(product=item.product,color=color)
                    return redirect('cart:cart',request.user.id)
                else:
                    
                    return redirect('cart:cart',request.user.id)
            else:
                return redirect('home:home')
        else:
                return redirect('home:home')
                        