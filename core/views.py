from django.shortcuts import render
from blog.models import Comentario

def Home(request):
    return render(request, 'core/home.html')

def lista_comentarios(request):
    comentarios = Comentario.objects.all()
    return render(request, 'core/lista_comentarios.html', {'comentarios': comentarios})
def productos(request):
    return render(request, 'core/productos.html')
def horario(request):
    return render(request, 'core/horario.html')
def about(request):
    return render(request, 'core/about.html')