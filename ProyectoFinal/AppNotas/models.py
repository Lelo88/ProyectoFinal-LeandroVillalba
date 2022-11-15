from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Etiqueta(models.Model):
    nombre_etiqueta = models.CharField(max_length=50)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.nombre_etiqueta

class Nota(models.Model):
    titulo = models.CharField(max_length = 200)
    cuerpo = models.CharField(max_length = 500)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    etiqueta = models.ForeignKey(Etiqueta, on_delete=models.CASCADE, null=True)
    
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizada = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['fecha_actualizada']
        
    def __str__(self) -> str:
        return self.titulo
    
    