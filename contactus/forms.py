from django import forms
from .models import Contact

class ContactUsForm(forms.ModelForm):
    
    class Meta:
        model = Contact
        fields = ('firstname','lastname','phonenumber','title','explanation')
        labels = {
            'firstname': ('نام'),
            'lastname': ('نام خانوادگی'),
            'phonenumber': ('شماره تماس'),
            'title': ('موضوع'),
            'explanation': ('پیام شما'),
        }
        
        widgets = {
            'explanation': forms.Textarea(attrs={'placeholder':'پیام خود را به صورت کامل و دقیق بنویسید'})
        }
        
        error_messages = {
            'firstname' : {
                'required' : 'فیلد نام الزامی است'
            },
            'lastname' : {
                'required' : 'فیلد نام خانوادگی الزامی است'
            },
            'phonenumber' : {
                'required' : 'فیلد شماره تماس الزامی است'
            },
            'title' : {
                'required' : 'فیلد موضوع الزامی است'
            },
            'explanation' : {
                'required' : 'فیلد پیام الزامی است'
            },
        }
             