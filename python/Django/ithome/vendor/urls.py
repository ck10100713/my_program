"""
URL configuration for ithome project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views
from .views import VendorListView, VendorDetailView, VendorCreateView, VendorUpdateView

# urlpatterns = [
#     path('', views.showtemplate),
# ]
app_name = 'vendors'
urlpatterns = [
    # path('', views.vendor_index, name='vendor_index'),
    path('', VendorListView.as_view(), name='index'),
    # path('create', views.vendor_create_view),
    path('create/', VendorCreateView.as_view(), name='create'),
    path('<int:pk>/', VendorDetailView.as_view(), name='vendor_id'),
    path('<int:pk>/update/', VendorUpdateView.as_view(), name='update'),
]