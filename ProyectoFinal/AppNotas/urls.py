from django.urls import path, include

from .views import inicio_nota

from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('notas/', inicio_nota, name = 'Notas'),
]