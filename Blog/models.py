from django.db import models



class Categoria (models.Model):
    nombre= models.CharField(max_length=50)
    created=models.DateTimeField(auto_now_add=True)
    updated= models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.nombre
    
    
class Blog(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField(max_length=10000)
    image = models.ImageField(upload_to='blogs')
    autor=models.CharField(max_length=50)
    created=models.DateTimeField(auto_now_add=True)
    updated= models.DateTimeField(auto_now_add=True)
    info=models.CharField(max_length=100, default=0)
    categoria=models.ManyToManyField(Categoria)
    
    def __str__(self):
      return self.nombre

class Comentario(models.Model):
    nombre = models.CharField(max_length=50)
    correo = models.EmailField()
    destino = models.CharField(max_length=50)
    comentario = models.TextField(max_length=50)
    blog=models.ForeignKey(Blog, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.nombre
