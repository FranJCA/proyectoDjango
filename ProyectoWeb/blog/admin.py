from django.contrib import admin
from .models import Categoria, Post #el .model recordar que es porque esta en la misma raiz donde admin.py estaubicado

# Register your models here.

class CategoriaAdmin(admin.ModelAdmin):
    readonly_fields=("created","updated")
    

class PostAdmin(admin.ModelAdmin):
    readonly_fields=("created", "updated")
    
admin.site.register(Categoria,CategoriaAdmin)

admin.site.register(Post,PostAdmin)
