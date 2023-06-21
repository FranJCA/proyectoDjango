from django.urls import path
from . import views
#como ya no se importa por ProyectoWebAPP solo se deja un .

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    
 #como esta dentro de appservicos no se nesesita aputnar con "servicios" solo apuntar a la raiz
    path('', views.servicios, name="servicios"),

]
 