from django import forms
from django.contrib.auth.models import User
from .models import Nota

class CrearNota(forms.ModelForm):
    
    class Meta:
        model = Nota
        fields = ['titulo', 'cuerpo']
        
class ActualizaNota(forms.ModelForm):
    
    class Meta:
        model = Nota 
        fields = ['titulo', 'cuerpo']

class ActualizaUsuario(forms.ModelForm):
    
    class Meta:
        model = User
        fields=['username', 'first_name', 'last_name']