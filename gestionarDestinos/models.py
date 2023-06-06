from django.db import models

# Create your models here.
class Destino(models.Model):
    lugar = models.CharField(max_length=50)
    actividad = models.CharField(max_length= 255)
    fecha = models.DateField()
    monto = models.IntegerField()
    lugar_recogida = models.CharField(max_length=255)
    img = models.ImageField()
    
    def __str__(self):
        return self.lugar

class Contacto(models.Model):
    nombre = models.CharField(max_length=50)
    correo = models.EmailField()
    asunto = models.CharField(max_length=255)
    mensaje = models.TextField()
    
    def __str__(self):
        return self.nombre
    
    