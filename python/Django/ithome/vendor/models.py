from django.db import models

from django.contrib import admin
# Create your models here.

class Vendor(models.Model):
    vendor_name = models.CharField(max_length=20)
    store_name = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.vendor_name

class Food(models.Model):
    food_name = models.CharField(max_length=30)
    food_price = models.DecimalField(max_digits=3, decimal_places=0)
    food_vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)

    def __str__(self):
        return self.food_name

from django.utils.translation import gettext_lazy as _

class Morethanfifty(admin.SimpleListFilter):
    title = _('price')
    # parameter_name is a formal attribute of the SimpleListFilter class
    # url first parameter
    parameter_name = 'compareprice'

    def lookups(self, request, model_admin):
        return (
            # first parameter is the value of the url parameter
            # second parameter is the description of the filter
            ('>50', _('more than 50')),
            ('<=50', _('less than 50')),
        )

    # queryset is a formal method of the SimpleListFilter class
    def queryset(self, request, queryset):
        if self.value() == '>50':
            # greater than
            return queryset.filter(food_price__gt=50)
        if self.value() == '<=50':
            # less than or equal to
            return queryset.filter(food_price__lte=50)

@admin.register(Vendor)
class VendorAdmin(admin.ModelAdmin):
    # list_display is a formal attribute of the ModelAdmin class
    # list_display = ('id', 'vendor_name', 'store_name', 'phone_number', 'address')
    list_display = [field.name for field in Vendor._meta.fields]

@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Food._meta.fields]
    # add a filter
    # filter depends on the field type
    # list_filter = ('food_price',)
    # filter depends on the our class
    list_filter = (Morethanfifty,)
    fields = ['food_price']
    # or
    # exclude = ['food_name', 'food_vendor']
    search_fields = ['food_name', 'food_price']
    # set the default ordering
    ordering = ['food_price']
    # if you want to set the default ordering to be the reverse of the default ordering
    # ordering = ['-food_price']
    # ordering = list_display