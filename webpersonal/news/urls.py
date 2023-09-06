from django.urls import path
from . import views

urlpatterns = [
    path('', views.news, name="news"),
    path('category/<int:categoryId>/', views.category, name="category"),
]