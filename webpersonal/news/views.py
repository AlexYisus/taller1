from django.shortcuts import render, get_object_or_404
from .models import News, Category
# Create your views here.

def news(request):
    news=News.objects.all()
    return render(request,"news/news.html",{'listnews':news})

def category(request, categoryID):
    category=get_object_or_404(Category, id=categoryID)
    news=News.object.filter(categories=category)
    return render(request, "news/category.html",{'listnews':news})