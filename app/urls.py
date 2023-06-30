from django.urls import path
from .views import *

urlpatterns = [
    # Aqui iran las URLS para accesos a pantallas del proyecto
    path('registro/', registro, name='registro'),
    path('', inicio, name='inicio'),
    path('login/', inicio_sesion, name='inicio_sesion'),
    path('ListadoClientes/',ListadoCliente, name="Listado"),
    path('ModificarCliente/<rut>/',ModificarCliente, name="Modificar"),
    path('EliminarCliente/<rut>/',EliminarCliente, name="Eliminar"),
    path('ConfirmarEliminar/<rut>/',ConfirmarEliminacionCliente, name="Confirmar"),
    
]
