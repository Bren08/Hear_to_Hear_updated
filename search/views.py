from django.shortcuts import render
from products.models import Aid

# Create your views here.
def do_search(request):
    products = Aid.objects.filter(name__icontains=request.GET['q'])
    return render(request, "products.html", {"products": products})
