from django.urls import path, include

from .views import loginView, registrar, editar_usuario

from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('registro/', registrar, name = 'Registro'),
    path('login/', loginView, name='Login'),
    path('', include('AppNotas.urls')),
    path('inicio/',LogoutView.as_view(template_name='inicio.html'), name='Logout' ),
    path('edita-usuario/', editar_usuario , name= 'Editar-Usuario')
]