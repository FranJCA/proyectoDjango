from django.urls import path
#from ProyectoWebAPP import views
from . import views

urlpatterns = [
    
    path('', views.contacto, name="contacto"),
    
    
    
]
