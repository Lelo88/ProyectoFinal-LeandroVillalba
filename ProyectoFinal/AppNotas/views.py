from django.shortcuts import render, redirect
from .models import Nota
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from .forms import CrearNota
# Create your views here.
def inicio_nota(request):
    notas = Nota.objects.all()
    return render(request, 'notas_inicio.html',{'notas': notas})

def agregado_notas(request):
    if request.method == 'POST':
        notas = CrearNota(request.POST)
        
        if notas.is_valid():
            nota = notas.save(commit = False)
            nota.autor =request.user
            nota.save()
            
            return redirect('Notas')
    else:
        notas = CrearNota()
            
    return render(request, 'agregado_notas.html',{'notas':notas})