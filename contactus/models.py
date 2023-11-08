from django.db import models
from django.forms import ValidationError
from django_jalali.db import models as jmodels
from django.contrib.auth.models import User

SITUATION_CHOICES = (
    ("Pending","Pending"),
    ("In Progress","In Progress"),
    ("Solved","Solved")
)

class Contact(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='contact_user',default=None)
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=30)
    phonenumber = models.CharField(max_length=11)
    title = models.CharField(max_length=50)
    explanation = models.TextField(max_length=500)
    situation = models.CharField(max_length=30,choices=SITUATION_CHOICES,default='Pending')
    created = jmodels.jDateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
    def clean(self):
        if len(self.phonenumber) < 11:
            raise ValidationError('شماره موبایل باید 11 رقم باشد')
        if len(self.phonenumber) > 11:
            raise ValidationError('شماره موبایل باید 11 رقم باشد')
        return super().clean()