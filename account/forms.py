from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from order.models import Order
from django.core.exceptions import ValidationError

class SignupForm(UserCreationForm):
    firstname = forms.CharField(label='',widget=forms.TextInput(attrs={'placeholder':'نام'}),error_messages={'required':'فیلد نام الزامی است'})
    lastname = forms.CharField(label='',widget=forms.TextInput(attrs={'placeholder':'نام خانوادگی'}),error_messages={'required':'فیلد نام خانوادگی الزامی است'})
    password1 = forms.CharField(label='',widget=forms.PasswordInput(attrs={'placeholder':'رمز عبور','data-toggle': 'password'}),error_messages={'required':'فیلد رمز عبور الزامی است'})
    password2 = forms.CharField(label='',widget=forms.PasswordInput(attrs={'placeholder':'تایید رمز عبور','data-toggle': 'password'}),error_messages={'required':'فیلد تایید رمز عبور الزامی است'})
    username = forms.CharField(label='',widget=forms.TextInput(attrs={'placeholder':'شماره موبایل'}),error_messages={'required':'فیلد شماره موبایل الزامی است'})
    verifycode = forms.CharField(label='',widget=forms.TextInput(attrs={'placeholder':'کد تایید'}),error_messages={'required':'فیلد کد تایید الزامی است'})
    
    def clean_username(self):
        username = self.cleaned_data['username']
        user = User.objects.filter(username=username).exists()
        if user:
            raise ValidationError('این شماره موبایل قبلا ثبت شده')
        if len(username) < 11:
            raise ValidationError('شماره موبایل باید 11 رقم باشد')
        if len(username) > 11:
            raise ValidationError('شماره موبایل باید 11 رقم باشد')
        if not username.startswith("09"):
            raise ValidationError('فرمت شماره موبایل وارد شده اشتباه است')
        return username
    
    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 != password2:
            raise ValidationError('رمز عبور مطابقت ندارد')
        if len(password1) < 8:
            raise ValidationError('رمز عبور باید بیشتر از 8 حرف باشد')
        return password2
    
    class Meta:
        model = User
        fields = ('firstname','lastname','password1','password2','username')
        
class LoginForm(forms.Form):
    username = forms.CharField(label='',widget=forms.TextInput(attrs={'placeholder':'شماره موبایل'}),error_messages={'required':'فیلد شماره موبایل الزامی است'})
    password = forms.CharField(label='',widget=forms.PasswordInput(attrs={'placeholder':'رمز عبور','data-toggle': 'password'}),error_messages={'required':'فیلد رمز عبور الزامی است'})
    
class ChangePasswordForm(forms.Form):
    oldpassword = forms.CharField(label='رمز عبور کنونی',widget=forms.PasswordInput())
    newpassword1 = forms.CharField(label='رمز عبور جدید',widget=forms.PasswordInput())
    newpassword2 = forms.CharField(label='تایید رمز عبور جدید',widget=forms.PasswordInput())
    
class EditUserProfileForm(forms.ModelForm):
    
    class Meta:
        model = User
        fields = ('first_name','last_name')
        labels = {
            'first_name': 'نام',
            'last_name' : 'نام خانوادگی'
        }
        
class EditOrderForm(forms.ModelForm):
    
    class Meta:
        model = Order
        fields = ('firstname','lastname','phonenumber','city','zipcode','fulladdress')
        labels = {
            'phonenumber': 'شماره تماس',
            'city': 'استان',
            'zipcode': 'کد پستی',
            'fulladdress': 'آدرس پستی',
            'firstname': 'نام',
            'lastname': 'نام خانوادگی'
        }
        
        widgets = {
            'phonenumber' : forms.TextInput(attrs={'required':True}),
            'city' : forms.Select(attrs={'required':True}),
            'zipcode' : forms.TextInput(attrs={'required':True}),
            'fulladdress' : forms.Textarea(attrs={'required':True}),
            'firstname' : forms.TextInput(attrs={'required':True}),
            'lastname' : forms.TextInput(attrs={'required':True}),
        }
