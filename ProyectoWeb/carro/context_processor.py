#variable global pyton/django conocido como context_processor



def importe_total_carro(request):
    total=0
    
    if request.user.is_authenticated:
      #  print(f"----{request.session}------")
      for key, value in request.session["carro"].items():
          total=total+(float(value["precio"]))
    else:
      total="debes hacer login"
    
    return{"importe_total_carro":total}





#toca ir a setting e ira a templates(proyectoweb) para que lea el contextprocesor