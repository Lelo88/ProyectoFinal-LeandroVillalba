from http.client import HTTPResponse
from django.shortcuts import render, redirect
from .models import Nota
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from .forms import CrearNota
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
# Create your views here.

@login_required
def inicio_nota(request):
    notas = Nota.objects.all()
    usuario=User.objects.all()
    if usuario.exists():
        return render(request, 'notas_inicio.html',{'notas': notas,'usuario':usuario})
    
    return render(request, 'notas_inicio.html',{'notas': notas})
    
def agregado_notas(request):
    
    if request.method == 'POST':
        notas = CrearNota(request.POST)
        
        if notas.is_valid():
            nota = notas.save(commit = False)
            nota.user =request.user
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

def edita_notas():
    pass