from django.shortcuts import render

# Create your views here.
from servicios.models import servicio
def servicios (request):
    
    servicios= servicio.objects.all() #importa todos los servicios construidos
    return render(request,"servicios/servicios.html",{"servicios":servicios})