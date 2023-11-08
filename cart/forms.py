from django import forms

class DiscountForm(forms.Form):
    code = forms.CharField(label='کد تخفیف دارید؟ وارد کنید')