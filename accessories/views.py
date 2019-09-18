from django.shortcuts import render
from .models import Accessories

# Create your views here.

def all_extras(request):
    extras = Accessories.objects.all()
    return render(request, "extras.html", {"extras": extras})