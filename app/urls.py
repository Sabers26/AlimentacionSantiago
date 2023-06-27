from django.urls import path
from .views import registro

urlpatterns = [
    # Aqui iran las URLS para accesos a pantallas del proyecto
    path('registro/', registro, name='registro'),
]
