from django.urls import path
from .views import registro, inicio, inicio_sesion

urlpatterns = [
    # Aqui iran las URLS para accesos a pantallas del proyecto
    path('registro/', registro, name='registro'),
    path('', inicio, name='inicio'),
    path('login/', inicio_sesion, name='inicio_sesion'),
]
