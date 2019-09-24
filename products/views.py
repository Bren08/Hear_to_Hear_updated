from django.shortcuts import render
from .models import Aid
from .models import Product_Addon

# Create your views here.

def all_products(request):
    products = Aid.objects.all()
    return render(request, "products.html", {"products": products})

def all_addons(request):
    addons = Product_Addon.objects.all()
    return render(request, "addons.html", {"addons": addons})
