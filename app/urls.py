from django.urls import path
from .views import *

urlpatterns = [
    # Aqui iran las URLS para accesos a pantallas del proyecto
    path('registro/', registro, name='registro'),
    path('', inicio, name='inicio'),
    path('login/', inicio_sesion, name='inicio_sesion'),
    path('logout/', cerrar_sesion, name='cerrar_sesion')
]
