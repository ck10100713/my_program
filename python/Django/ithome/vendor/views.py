from django.shortcuts import render
from .models import Vendor
from .forms import VendorForm, RawVendorForm

# Create your views here.
def vendor_index(request):
    vendor_list = Vendor.objects.all()
    context = {'vendor_list': vendor_list}
    return render(request, 'vendor/detail.html', context)

def vendor_create_view(request):

    form = RawVendorForm(request.POST or None)
    if form.is_valid():
        Vendor.objects.create(**form.cleaned_data)
        print(form.cleaned_data)
        form = RawVendorForm()
    context = {'form': form}
    return render(request, 'vendor/vendor_create.html', context)

from django.http import Http404
from django.shortcuts import get_object_or_404

def single_Vendor(request, id):
    # try:
    #     vendor_lists = Vendor.objects.get(id=id)
    # except Vendor.DoesNotExist:
    #     raise Http404("Vendor does not exist")
    
    vendor_lists = get_object_or_404(Vendor, id=id)
    context = {'vendor_list': vendor_lists}
    return render(request, 'vendor/vendor_detail.html', context)