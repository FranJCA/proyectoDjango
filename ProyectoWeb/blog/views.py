from django.shortcuts import render
from blog.models import Post,Categoria
# Create your views here.

def blog (request):
    
    post= Post.objects.all()
    return render(request,"blog/blog.html",{"post":post})

def categoria(request, categoria_id):
    categoria = Categoria.objects.get(id=categoria_id)
    post = Post.objects.filter(categorias=categoria)
    return render(request, "blog/categoria.html", {"categoria": categoria, "post": post})
#para hacerlo funcionar localhost:8000/blog/categoria/id

