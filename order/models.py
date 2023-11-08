from django.db import models
from products.models import Product
from django.contrib.auth.models import User

CITY_CHOICES = (
    ("آذربایجان شرقی","آذربایجان شرقی"),
    ("آذربایجان غربی","آذربایجان غربی"),
    ("اردبیل","اردبیل"),
    ("اصفهان","اصفهان"),
    ("البرز","البرز"),
    ("ایلام","ایلام"),
    ("بوشهر","بوشهر"),
    ("تهران","تهران"),
    ("چهارمحال و بختیاری","چهارمحال و بختیاری"),
    ("خراسان جنوبی","خراسان جنوبی"),
    ("خراسان رضوی","خراسان رضوی"),
    ("خراسان شمالی","خراسان شمالی"),
    ("خوزستان","خوزستان"),
    ("زنجان","زنجان"),
    ("سمنان","سمنان"),
    ("سیستان و بلوچستان","سیستان و بلوچستان"),
    ("فارس","فارس"),
    ("قزوین","قزوین"),
    ("قم","قم"),
    ("کردستان","کردستان"),
    ("کرمان","کرمان"),
    ("کرمانشاه","کرمانشاه"),
    ("کهگیلویه وبویراحمد","کهگیلویه وبویراحمد"),
    ("گلستان","گلستان"),
    ("گیلان","گیلان"),
    ("لرستان","لرستان"),
    ("مازندران","مازندران"),
    ("مرکزی","مرکزی"),
    ("هرمزگان","هرمزگان"),
    ("همدان","همدان"),
    ("یزد","یزد"),
)

class Order(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name='order_product1',default=None)
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='order_user')
    ordertracking = models.CharField(max_length=15,null=True,blank=True)
    phonenumber = models.CharField(max_length=11,null=True,blank=True)
    firstname = models.CharField(max_length=20,null=True,blank=True)
    lastname = models.CharField(max_length=20,null=True,blank=True)
    totalprice = models.CharField(max_length=12)
    city = models.CharField(max_length=50,choices=CITY_CHOICES,null=True,blank=True,)
    zipcode = models.BigIntegerField(null=True,blank=True)
    fulladdress = models.TextField(null=True,blank=True)
    description = models.TextField(null=True,blank=True)
    authority = models.CharField(max_length=100,default=None,blank=True,null=True)
    paid = models.BooleanField(default=False)
    postdelivered = models.BooleanField(default=False)
    posttracking = models.CharField(max_length=50,null=True,blank=True)
    orderpreparing = models.BooleanField(default=False)
    
class OrderProduct(models.Model):
    order = models.ForeignKey(Order,on_delete=models.CASCADE,related_name='order')
    product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name='order_product')
    color = models.CharField(max_length=30)