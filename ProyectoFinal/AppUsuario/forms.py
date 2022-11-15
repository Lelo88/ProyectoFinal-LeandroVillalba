from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from django.contrib.auth.models import User

class UserRegisterForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ['first_name', 'last_name' ,'username', 'email', 'password1', 'password2']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'login__input', 'id':'login-input-user'}),
            'last_name': forms.TextInput(attrs={'class': 'login__input', 'id':'login-input-user'}), 
            'username': forms.TextInput(attrs={'class': 'login__input', 'id':'login-input-user'}),
            'email': forms.EmailInput(attrs={'class': 'login__input', 'id':'login-input-user'}),
            'password1': forms.PasswordInput(attrs={'class':'login__input','id':'login-input-password'}),
            'password2': forms.PasswordInput(attrs={'class':'login__input','id':'login-input-password'}),
        }

class Autenticacion(AuthenticationForm):
    
    class Meta: 
        model = User
        fields = ['username', 'email', 'password']
        widgets = {
            'username': forms.TextInput(attrs={'class':'login__input', 'id':'login-input-user'}),
            'email': forms.EmailInput(attrs={'class':'login__input', 'id':'login-input-user'}),
            'password': forms.PasswordInput(attrs={'class':'login__input','id':'login-input-password1'})
        }