from django.db import models
#inmportacion de la libreria User para permitir el funcionamiento
#de  autor=models.ForeignKey(User, on_delete==models.CASCADE)
    
from django.contrib.auth.models import User



# Create your models here.

class Categoria(models.Model):
    nombre=models.CharField(max_length=50)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)
    
    class Meta:    
        
        verbose_name= "categoria"
        verbose_name_plural="categoria"
        
    def __str__(self):
        return self.nombre
    
class Post(models.Model):
    titulo=models.CharField(max_length=50)
    contenido=models.CharField(max_length=50)
    imagen=models.ImageField(upload_to="blog",null=True,blank=True)#permite dejar el campo de la imagen vacio 
    autor=models.ForeignKey(User, on_delete=models.CASCADE)
    categorias= models.ManyToManyField(Categoria) #establecer la relacion de las 2 base de datos
    
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)
    
    class Meta:    
        
        verbose_name= "post"
        verbose_name_plural="post"
        
    def __str__(self):
        return self.titulo
    
