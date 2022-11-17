from http.client import HTTPResponse
from django.shortcuts import render, redirect
from .models import Nota
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from .forms import CrearNota, ActualizaNota
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
# Create your views here.

@login_required
def inicio_nota(request):
    usuario=request.user.id
    notas = Nota.objects.filter(autor=usuario)
    return render(request, 'notas_inicio.html',{'notas': notas})
    
    
def agregado_notas(request):
    
    if request.method == 'POST':
        notas = CrearNota(request.POST)
        
        if notas.is_valid():
            info_notas = notas.cleaned_data
            nota = Nota(titulo = info_notas['titulo'], cuerpo = info_notas['cuerpo'], autor = request.user)
            nota.autor =request.user
            nota.save()        
            
            return redirect('Notas')
    else:
        notas = CrearNota()
            
    return render(request, 'agregado_notas.html',{'notas':notas})

def borrar_notas(request, id):
    
    nota = Nota.objects.get(id=id)
    nota.delete()
    messages.success(request, 'Esta nota fue borrada!')

    return redirect('Notas')

def edita_notas(request, id):
    nota_actualizada = Nota.objects.get(id=id)
    formulario_edicion = ActualizaNota(instance = nota_actualizada)
    
    if request.metod == 'POST':
        formulario_edicion = ActualizaNota(request.POST)
        
        if formulario_edicion. is_valid():
            
            nota_actualizada.titulo = formulario_edicion['titulo']
            nota_actualizada.cuerpo = formulario_edicion['cuerpo']
            
            nota_actualizada.save()
            
            return redirect('Notas')