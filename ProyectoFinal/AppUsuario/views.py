from django.shortcuts import render

from django.shortcuts import render, redirect
from .forms import UserRegisterForm, Autenticacion, EditaUsuario
from django.contrib.auth import authenticate, login
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from django.contrib.auth.models import User



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
        formulario_avatar = FormAvatar(request.user.id) #esta linea aggrego
        
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
                return redirect('Notas')            
            else:
                return redirect('Login')
        
        return redirect('Login')
    
    else: 
        
        mi_formulario = Autenticacion()
        
        return render(request, "login.html", {"mi_formulario": mi_formulario})

def editar_usuario(request):
    
    usuario = request.user
    
    
    if request.method == 'POST':
        
        formulario_usuario = EditaUsuario(request.POST)
        
        if formulario_usuario.is_valid():
            
            data = formulario_usuario.cleaned_data
            
            usuario.first_name = data['first_name']
            usuario.last_name = data['last_name']
            usuario.username = data['username']
            usuario.email = data['email']
            usuario.set_password(data['password1'])
            
            usuario.save()
            
            return redirect('Inicio')
        return redirect('Edita-Usuario')
    
    else:
        formulario_usuario = EditaUsuario(instance = request.user)
        
        return render(request,'edita-perfil.html', {'formulario_usuario': formulario_usuario})
