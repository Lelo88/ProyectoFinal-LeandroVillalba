from django.shortcuts import render
from .models import Nota
# Create your views here.
def inicio_nota(request):
    notas = Nota.objects.all()
    return render(request, 'notas_inicio.html',{'notas': notas})

