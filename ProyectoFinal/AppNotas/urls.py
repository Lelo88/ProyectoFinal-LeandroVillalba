from django.urls import path, include

from .views import inicio_nota, agregado_notas


urlpatterns = [
    path('notas/', inicio_nota, name = 'Notas'),
    path('agregado-notas/', agregado_notas, name='Agregado-Notas')
]