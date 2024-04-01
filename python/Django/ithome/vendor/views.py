from django.shortcuts import render
from .models import Vendor
from .forms import VendorForm, RawVendorForm

# Create your views here.
def vendor_index(request):
    vendor_list = Vendor.objects.all()
    context = {'vendor_list': vendor_list}
    return render(request, 'vendor\detail.html', context)

def vendor_create_view(request):
    form = RawVendorForm(request.POST or None)
    if form.is_valid():
        Vendor.objects.create(**form.cleaned_data)
        print(form.cleaned_data)
        form = RawVendorForm()
    context = {'form': form}
    return render(request, 'vendor/vendor_create.html', context)

def single_Vendor(request, id):
    print(Vendor.objects.all())
    vendor_list = Vendor.objects.get(id=id)
    context = {'vendor_list': vendor_list}
    print(context)
    return render(request, 'vendor/vendor_detail.html', context)