from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator 
from django_jalali.db import models as jmodels

class DiscountCode(models.Model):
    code = models.CharField(max_length=15)
    discount = models.IntegerField(default=0,validators=[MinValueValidator(1),MaxValueValidator(100)])
    created = jmodels.jDateTimeField(auto_now_add=True)
    
class AdminModel(models.Model):
    buy = models.BooleanField(default=True)