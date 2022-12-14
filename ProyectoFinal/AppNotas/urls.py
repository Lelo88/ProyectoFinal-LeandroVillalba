from django.urls import path, include

from .views import borrar_notas, inicio_nota, agregado_notas, edita_notas


urlpatterns = [
    path('notas/', inicio_nota, name = 'Notas'),
    path('agregado-notas/', agregado_notas, name='Agregado-Notas'),
    path('borrado-notas/<int:id>', borrar_notas, name='Borrar-Notas'), 
    path('editado-notas/<int:id>', edita_notas, name ='Editado-Notas')
]