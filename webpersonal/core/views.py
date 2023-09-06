from django.shortcuts import render

# Create your views here.
htmlBase = """"
  
"""
def home(request):
    return render(request, "core/home.html")


def about(request):
    return render(request, "core/about.html")


def shop(request):

    return render(request, "core/shop.html")


def shopsingle(request):

    return render(request, "core/shopsingle.html")

def contact(request):

    return render(request, "core/contact.html")
