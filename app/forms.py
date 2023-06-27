from django.forms import ModelForm
from . import models

#Formulario de registro de cuenta de usuario
def RegistroForm(ModelForm):
    
    class Meta:
        model = models.Cliente
        fields = ['rut', 'dv', 'nombre', 'apellido1', 'apellido2', 'correo']