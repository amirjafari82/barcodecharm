from django.db import models
from django.contrib.auth.models import User
from django_jalali.db import models as jmodels
from django.core.validators import MaxValueValidator,MinValueValidator

class Product(models.Model):
    title = models.CharField(max_length=80)
    peresentimage = models.ImageField(upload_to='static/images/products',default=None)
    price = models.CharField(max_length=12)
    features = models.TextField()
    description = models.TextField()
    number = models.PositiveIntegerField()
    colors = models.CharField(max_length=200)
    slug = models.SlugField(auto_created=True,unique=True,allow_unicode=True)
    created = jmodels.jDateTimeField(auto_now_add=True)
    updated = jmodels.jDateTimeField(auto_now=True)
    discount = models.BooleanField(default=False)
    offprice = models.CharField(blank=True,null=True,max_length=12)

    
    class Meta:
        ordering = ('created',)
        
    def __str__(self):
        return f'{self.title} - {self.created}'
    
class ProductImage(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name='product_image')
    image = models.ImageField(upload_to='static/images/products')
    color = models.CharField(max_length=200,default=None,null=True,blank=True)
    
class Comment(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='user_comment')
    product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name='product_comment')
    body = models.TextField(max_length=120)
    score = models.IntegerField(default=0,validators=
        [
            MaxValueValidator(5),
            MinValueValidator(0)
        ])
    approved = models.BooleanField(default=False)
    created = jmodels.jDateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.user} - {self.body[:20]}'