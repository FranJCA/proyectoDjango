from django.shortcuts import render,redirect
from .forms import  FormularioContacto

from django.core.mail import EmailMessage



# Create your views here.

def contacto (request):

    formulario_contacto=FormularioContacto()

    if request.method=="POST":
        formulario_contacto=FormularioContacto(data=request.POST)
        if formulario_contacto.is_valid():
            nombre=request.POST.get("nombre")
            email=request.POST.get("email")
            contenido=request.POST.get("contenido")
            #redireccione a contacto
            # email=EmailMessage("Mensaje desde app Django",
            # "El usuario con nombre {} con la direccion {} escribe lo sigiente{}:\n\n{}".format(nombre,email,contenido),"",["aqui va un correo electronico"],reply_to=[email])
            email = EmailMessage(
                "Mensaje desde app Django",
                "El usuario con nombre {} con la dirección {} escribe lo siguiente:\n\n{}".format(nombre, email, contenido),
                "",
                [],
                reply_to=[email]
            )
            
            try:
                email.send()

                return redirect("/contacto/?valido") #el ? no es un error es importante o sino se rompe la pagina

            except:

                return redirect("/contacto/?Novalido") #el ? no es un error es importante o sino se rompe la pagina




    return render(request,"contacto/contacto.html",{"miformulario":formulario_contacto})



