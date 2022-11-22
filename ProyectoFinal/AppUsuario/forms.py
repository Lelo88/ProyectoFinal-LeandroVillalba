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
        
class EditaUsuario(UserChangeForm):
    password = forms.CharField(
        help_text = "",
        widget= forms.HiddenInput(), required = False
    )
    username=forms.CharField(required=False)
    email=forms.CharField(required=False)
    password1 = forms.CharField(label = "Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label = "Repita la contraseña", widget=forms.PasswordInput)
    
    class Meta: 
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']
        
        
    def clean_password2(self):
        password2 = self.cleaned_data['password2']
        if password2 != self.cleaned_data['password1']:
            raise forms.ValidationError('¡No coinciden las contraseñas!')
        return password2 