from django.shortcuts import render
from .models import Promotion

# Create your views here.

def promotion(request):
    promotion=Promotion.objects.all()
    return render(request, "promotion/promotion.html",{'listpromotion':promotion})