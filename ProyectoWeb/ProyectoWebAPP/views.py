from django.shortcuts import render, HttpResponse

from carro.carro import Carro 





# Create your views here.
def home (request):
    carro= Carro(request) #es importante esta linea de codigo o dara dolores de cabeza despues
    return render(request,"ProyectoWebAPP/home.html")





# -------------old
# def servicios (request):
    
#     servicios= servicios.objects.all()
#     return render(request,"ProyectoWebAPP/servicios.html")