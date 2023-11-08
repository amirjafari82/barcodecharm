from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView
from django.contrib.auth.views import LogoutView 
from django.contrib.auth.models import User
from .forms import SignupForm, LoginForm, ChangePasswordForm, EditUserProfileForm, EditOrderForm
from django.contrib import messages
from order.models import Order, OrderProduct
from contactus.models import Contact
from products.models import ProductImage
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
import json, requests

class SignupView(CreateView):
    template_name = 'account/signup.html'
    success_url = reverse_lazy('account:login')
    form_class = SignupForm
    
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home:home')
        return super().dispatch(request, *args, **kwargs)
    
    def form_valid(self,form):
        new_user = form.save(commit=False)
        new_user.first_name = form.cleaned_data['firstname']
        new_user.last_name = form.cleaned_data['lastname']
        new_user.save
        messages.success(self.request,'ثبت نام با موفقیت انجام شد','success')
        return super().form_valid(form)
    
class SendCode(View):
    
    def post(self,request):
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            phone = request.POST.get('phone')
            code = request.POST.get('code')
            url = "https://ippanel.com/api/select"
            payload = json.dumps({
                "op" : "pattern",
	            "user":"09398708391",
		    	"pass":"13829162Am",
		    	"fromNum":"+983000505",
		    	"toNum":phone,
		    	"patternCode":"h2i0to5kcyjrvld",
		    	"inputData":[
		    			{"verify-code":code},	
		    		]
            })
            headers = {
                'Content-Type': 'application/json'
            }
            response = requests.request("POST", url, headers=headers, data=payload)
            return JsonResponse({'status':'ok','code':code})
    
class UserLoginView(View):
    form_class = LoginForm
    
    def get(self,request):
        if request.user.is_authenticated:
            return redirect('home:home')
        return render(request,'account/login.html',{'form':self.form_class})
    
    def post(self,request):
        form = self.form_class(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request,username=username,password=password)
            if user is not None:
                messages.success(request,'وارد شدید','success')
                login(request,user)
            else:
                messages.error(request,'شماره تماس یا رمز عبور اشتباه است','danger')
                return redirect('account:login')
        return redirect('home:home')
    
class UserLogout(LogoutView):
    next_page = reverse_lazy('home:home')
    
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            messages.success(request,'خارج شدید','success')
        return super().dispatch(request, *args, **kwargs)
    

class ProfileView(LoginRequiredMixin,View):
    
    def get(self,request,user_id):
        if request.user.id == user_id:
            user = User.objects.get(id=user_id)
            orders = Order.objects.filter(user=user)
            products = OrderProduct.objects.all()
            productimages = ProductImage.objects.all()
            contacts = Contact.objects.filter(user=user)
            return render(request,'account/profile.html',{'user':user,'products':products,'orders':orders,'productimages':productimages,'contacts':contacts})
        else:
            return redirect('home:home')
        
class ChangePassword(LoginRequiredMixin,View):
    form_class = ChangePasswordForm
    
    def get(self,request,user_id):
        if request.user.id == user_id:
            return render(request,'account/changepassword.html',{'form':self.form_class})
        else:
            return redirect('home:home')
        
    def post(self,request,user_id):
        form = self.form_class(request.POST)
        if form.is_valid():
            oldpassword = form.cleaned_data['oldpassword']
            if self.request.user.check_password(oldpassword):
                newpassword1 = form.cleaned_data['newpassword1']
                newpassword2 = form.cleaned_data['newpassword2']
                if newpassword1 == newpassword2:
                    if len(newpassword1) > 8:
                        user = User.objects.get(id=user_id)
                        user.set_password(newpassword1)
                        user.save()
                        messages.success(request,'رمز عبور شما با موفقیت عوض شد. دوباره وارد شوید','success')
                        return redirect('account:profile',user_id)
                    else:
                        messages.error(request,'رمز عبور جدید کمتر از 8 کاراکتر است','danger')
                        return redirect('account:change-password',user_id)
                else:
                    messages.error(request,'رمز عبور جدید و تایید رمز عبور مطابقت ندارد','danger')
                    return redirect('account:change-password',user_id)
            else:
                messages.error(request,'رمز عبور کنونی اشتباه است','danger')
                return redirect('account:change-password',user_id)
        return redirect('account:change-password',user_id)
    
class EditUserProfile(LoginRequiredMixin,View):
    form_class = EditUserProfileForm
    
    def get(self,request,user_id):
        if request.user.id == user_id:
            form = self.form_class(instance=request.user)
            return render(request,'account/editprofile.html',{'form':form})
        else:
            return redirect('home:home')
    
    def post(self,request,user_id):
        form = self.form_class(request.POST,instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request,'پروفایل ویرایش شد','danger')
            return redirect('account:profile',user_id)
        
class EditOrder(LoginRequiredMixin,View):
    form_class = EditOrderForm
    
    def get(self,request,order_id):
        order = get_object_or_404(Order,id=order_id)
        form = self.form_class(instance=order)
        if request.user == order.user:
            if order.paid == True and order.postdelivered == False:
                return render(request,'account/editorder.html',{'form':form})
            else:
                return redirect('home:home')
        else:
            return redirect('home:home')
    
    def post(self,request,order_id):
        order = get_object_or_404(Order,id=order_id)
        form = self.form_class(request.POST,instance=order)
        if form.is_valid():
            form.save()
            messages.success(request,'با موفقیت ویرایش شد','success')
            return redirect('account:profile',order.user.id)
        
class SeeOrderDetail(LoginRequiredMixin,View):
    
    def get(self,request,order_id):
        order = Order.objects.get(id=order_id)
        products = order.order.all()
        colorlist = {}
        for product in products:
            new_list = product.color.replace("'",'').strip('][').split(', ')
            colorlist[product.id] = {'color': new_list}
        for id,color in colorlist.items():
            print(id, color['color'])
        return render(request,'account/orderdetail.html',{'order':order,'colors':colorlist})