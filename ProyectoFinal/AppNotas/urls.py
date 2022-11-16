from django.urls import path, include

from .views import notas

from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('notas/', notas, name = 'Notas'),
]