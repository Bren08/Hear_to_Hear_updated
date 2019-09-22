from django.shortcuts import render
from products.models import Aid


# Create your views here.
def search_products(request):
    products = Aid.objects.filter(brand__icontains=request.GET['q'])
    return render(request, "products.html", {"products": products})

