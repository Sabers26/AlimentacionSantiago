from django import forms
from .models import Cliente, validar_rut, validar_nombre

#Formulario de registro de cuenta de usuario
class RegistroForm(forms.ModelForm):
    
    def clean_rut(self):
        rut = self.cleaned_data['rut']
        validar_rut(rut)
        return rut

    def clean_nombre(self):
        nombre = self.cleaned_data['nombre']
        validar_nombre(nombre)
        return nombre
    
    def clean_apellido(self):
        apellido = self.cleaned_data['apellido']
        validar_nombre(apellido)
        return apellido
    class Meta:
        model = Cliente
        fields = ['rut', 'dv', 'nombre', 'apellido', 'correo']

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['rut','dv','nombre','apellido','correo']
        widgets = {
        'rut' : forms.TextInput(attrs={'class':'controls'}),
        'dv' : forms.TextInput(attrs={'class':'controls'}),
        'nombre' : forms.TextInput(attrs={'class':'controls'}),
        'apellido' : forms.TextInput(attrs={'class':'controls'}),
        'correo' : forms.TextInput(attrs={'class':'controls'}),
        }