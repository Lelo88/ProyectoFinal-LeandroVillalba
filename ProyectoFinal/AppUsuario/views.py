from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .forms import UserRegisterForm, Autenticacion
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def registrar(request):
    
    if request.method == 'POST':
        mi_formulario = UserRegisterForm(request.POST)
        if mi_formulario.is_valid():
            
            nom_usuario = mi_formulario.cleaned_data['username']
            mi_formulario.save()
            
            return render(request, 'inicio.html', {'mensaje': f'Usuario {nom_usuario} creado con exito'})
        
        else: 
            
            return render(request, 'inicio.html', {'mensaje': 'Error al crear el usuario'})
    
    else: 
        
        mi_formulario = UserRegisterForm()
        
        return render(request, 'registro.html', {'mi_formulario': mi_formulario})
    
def loginView(request):
    
    if request.method == 'POST':
        mi_formulario = Autenticacion(request, data = request.POST)
        
        if mi_formulario.is_valid():
            data = mi_formulario.cleaned_data
            
            usuario = data['username']
            contraseña = data['password']
            
            user = authenticate(username = usuario, password=contraseña)
            
            if user:
                
                login(request, user)
                return render(request, 'notas_inicio.html')
                #return render(request, '/ProyectoFinal/AppNotas/templates/notas.html', {'mensaje' : f'Bienvenido {usuario}'})
            
            else:
                return redirect('Login')
        
        return redirect('Login')
    
    else: 
        
        mi_formulario = Autenticacion()
        
        return render(request, "login.html", {"mi_formulario": mi_formulario})

# Create your views here.
