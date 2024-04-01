from django import forms
from .models import Vendor, Food

from django.utils.translation import gettext_lazy as _ # 新增

class VendorForm(forms.ModelForm):
    class Meta:
        model = Vendor
        fields = '__all__'
        # 新增 labels 對應
        labels = {
            'vendor_name': _('vendor_name'),
            'store_name' : _('store_name'),
            'phone_number' : _('phone_number'),
            'address' : _('address'),
        }

class RawVendorForm(forms.Form):
    vendor_name = forms.CharField(label='vendor_name', widget=forms.TextInput(attrs={"placeholder": "Your vendor_name"}))
    store_name = forms.CharField(label='store_name', widget=forms.TextInput(attrs={"placeholder": "Your store_name"}))
    phone_number = forms.CharField(label='phone_number', widget=forms.TextInput(attrs={"placeholder": "Your phone_number"}))
    address = forms.CharField(label='address', widget=forms.TextInput(attrs={"placeholder": "Your address"}))