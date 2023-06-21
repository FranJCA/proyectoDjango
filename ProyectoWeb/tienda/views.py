from django.shortcuts import render

# Create your views here.

# def tienda (request):
#     return render(request,"tienda/tienda.html")

from .models import Producto

def tienda(request):
    productos = Producto.objects.all()
    return render(request,"tienda/tienda.html",{"productos":productos} )


