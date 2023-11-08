from django import forms
from products.models import Product, ProductImage, Comment
from multiupload.fields import MultiImageField
from weblog.models import Article
from .models import DiscountCode
from order.models import Order
from contactus.models import Contact

class AddProductForm(forms.ModelForm):
    peresentimage = forms.ImageField(label='عکس (عکسی که در لیست محصولات نمایش داده میشود)',required=False)
    class Meta:
        model = Product
        fields = ['title','peresentimage','price','features','description','number','colors']
        labels = {
            'title': 'عنوان کالا',
            'price': 'قیمت',
            'features': 'مشخصات',
            'description': 'توضیحات',
            'number': 'تعداد',
            'colors': 'رنگ ها',
        }
        
class AddProductImageForm(forms.ModelForm):
    image = MultiImageField(label='عکس ها',min_num=1,max_num=6)
    
    class Meta:
        model = ProductImage
        fields = ('image',)
        
class UpdateProductForm(forms.ModelForm):
    
    class Meta:
        model = Product
        fields = ['peresentimage','title','price','features','description','number','colors','discount','offprice']
        labels = {
            'title': 'عنوان کالا',
            'price': 'قیمت',
            'features': 'مشخصات',
            'description': 'توضیحات',
            'number': 'تعداد',
            'colors': 'رنگ ها',
            'peresentimage': 'عکس (عکسی که در لیست محصولات نمایش داده میشود)',
            'discount': 'تخفیف',
            'offprice': 'قیمت پس از تخفیف'
        }
        
class AddArticleForm(forms.ModelForm):
    
    class Meta:
        model = Article
        fields = ('image','title','text')
        labels = {
            'image': 'عکس',
            'title': 'موضوع',
            'text': 'متن',
        }
        

class UpdateArticleForm(forms.ModelForm):
    
    class Meta:
        model = Article
        fields = ('image','title','text')
        labels = {
            'image': 'عکس',
            'title': 'موضوع',
            'text': 'متن',
        }
        
class AddDiscountForm(forms.ModelForm):
    
    class Meta:
        model = DiscountCode
        fields = ('code','discount')
        labels = {
            'code': 'کد تخفیف',
            'discount': 'درصد تخفیف (بین 1 تا 100 بدون علامت %)'
        }

class ChangeOrderStatusForm(forms.ModelForm):
    
    class Meta:
        model = Order
        fields = ('orderpreparing','postdelivered','posttracking')
        labels = {
            'orderpreparing': 'در حال آماده سازی سفارش',
            'postdelivered': 'تحویل داده شده به پست',
            'posttracking': 'کد رهگیری پست'
        }
        
class ChangeContactSituation(forms.ModelForm):
    
    class Meta:
        model = Contact
        fields = ('situation',)
        labels = {
            'situation': 'وضعیت',
        }
        
class OrderSearchForm(forms.Form):
    search = forms.CharField(label='جستجو بر اساس کد رهگیری')
    
class ApproveCommentForm(forms.ModelForm):
    
    class Meta:
        model = Comment
        fields = ("approved",)
        labels = {
            'approved': 'تایید',
        }