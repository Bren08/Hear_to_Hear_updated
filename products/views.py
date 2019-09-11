from django.shortcuts import render
from .models import Aid

# Create your views here.

def all_products(request):
    products = Aid.objects.all()
    return render(request, "products.html", {"products": products})