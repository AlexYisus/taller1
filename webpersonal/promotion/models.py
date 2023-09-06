from django.db import models

# Create your models here.

class Promotion(models.Model):
    title=models.CharField(max_length=100, verbose_name="Titulo")
    subtitle=models.CharField(max_length=100, verbose_name="Subtitulo")
    image=models.ImageField(verbose_name="Imagen", upload_to="promotion")
    content=models.TextField(verbose_name="Contenido")
    created=models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated=models.DateTimeField(auto_now=True, verbose_name="Fecha de modificación")


    class Meta:
        verbose_name="Promoción"
        verbose_name_plural="Promociones"
        ordering=["created"]

    def __str__(self):
        return self.title