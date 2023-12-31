from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    name=models.CharField(max_length=50, verbose_name="Nombre")
    created=models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated=models.DateTimeField(auto_now_add=True, verbose_name="Fecha de modificación")

    class Meta:
        verbose_name="Categoría"
        verbose_name_plural="Categorías"
        ordering=["name"]

    def __str__(self):
        return self.name

class News(models.Model):
    title=models.CharField(max_length=100, verbose_name="Título")
    content=models.TextField(verbose_name="Contenido")
    price=models.BooleanField(max_length=5, verbose_name="Precio")
    published=models.DateTimeField(verbose_name="Fecha de publicación", default=now)
    image=models.ImageField(verbose_name="Imagen", upload_to="news")
    author= models.ForeignKey(User, verbose_name="Autor", on_delete=models.CASCADE)
    categories=models.ManyToManyField(Category, verbose_name="Categorias")
    created=models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated=models.DateTimeField(auto_now_add=True, verbose_name="Fecha de modificación")

    class Meta:
        verbose_name="Entrada"
        verbose_name_plural="Entradas"
        ordering=["-created"]

    def __str__(self):
        return self.title