from django.db import models

# Create your models here.

class CategoriaProd(models.Model):
    nombre = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "categoriaProd"
        verbose_name_plural = "categoriasProd"
        
    def __str__(self):
        return self.nombre



class Producto(models.Model):
    nombre=models.CharField(max_length=150)
    categorias= models.ForeignKey(CategoriaProd, on_delete=models.CASCADE) #esto sirve para cunado se elimine un objeto que se quiera eliminar se elimine en cascada
    imagen= models.ImageField(upload_to="tienda",null=True,blank=True) #recuerda tener instalado el pillow
    precio=models.FloatField()
    disponibilidad= models.BooleanField(default=True)
    
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name="Producto"
        verbose_name_plural="Productos"
    
#recuerda hacer las migraciones
#en una tabla ya creada  modificar un modelo despues de haberlas creada django va a preguntar 2 
#cosas si deja un valor prodeecto generado por el sistema o abortar y modificar el modelo para que se le asigne un valor pro defecto esto es debio a que no puede dejar campos vacios