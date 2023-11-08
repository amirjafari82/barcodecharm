from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import FormView
from .forms import ContactUsForm
from django.contrib import messages

class ContactUs(FormView):
    template_name = 'contactus/contactus.html'
    form_class = ContactUsForm
    success_url = reverse_lazy('home:home')
    
    def form_valid(self, form):
        new_contact = form.save(commit=False)
        new_contact.user = self.request.user
        new_contact.save()
        messages.success(self.request,'پیام شما با موفقیت ثبت شد','success')
        return super().form_valid(form)