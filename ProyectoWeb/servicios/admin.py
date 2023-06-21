from django.contrib import admin

# Register your models here.
from .models import servicio

class ServicioAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')

admin.site.register(servicio,ServicioAdmin)