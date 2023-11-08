from django import forms
from .models import Order

class DiscountForm(forms.Form):
    code = forms.CharField(label='کد تخفیف دارید؟ وارد کنید')
    
class OrderForm(forms.ModelForm):
    
    class Meta:
        model = Order
        fields = ('firstname','lastname','phonenumber','city','zipcode','fulladdress','description')
        labels = {
            'phonenumber': 'شماره تماس',
            'city': 'استان',
            'zipcode': 'کد پستی',
            'fulladdress': 'آدرس پستی',
            'firstname': 'نام',
            'lastname': 'نام خانوادگی',
            'description': 'توضیحات (سایز پین و سایز مچ خود را به صورت دقیق وارد کنید)'
        }
        
        widgets = {
            'phonenumber' : forms.TextInput(attrs={'required':True}),
            'city' : forms.Select(attrs={'required':True}),
            'zipcode' : forms.TextInput(attrs={'required':True}),
            'fulladdress' : forms.Textarea(attrs={'required':True}),
            'firstname' : forms.TextInput(attrs={'required':True}),
            'lastname' : forms.TextInput(attrs={'required':True}),
            'description': forms.Textarea(attrs={'required':True,'placeholder':'سایز مچ : 18 سانتی متر ، سایز پین : 19 سانتی متر'}),
        }