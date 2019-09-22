from django.shortcuts import render
from .models import Accessories

# Create your views here.

def all_accessories(request):
    accessory = Accessories.objects.all()
    return render(request, "accessories.html", {"accessory": accessory})