from django.db import models
from django.core.validators import RegexValidator, MinLengthValidator, MinValueValidator, MaxLengthValidator, MaxValueValidator
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
# Create your models here.

#Validacion de los campos de usuario
def validar_rut(value):
    error = 'El rut ingresado no es valido. Ingreselo sin puntos ni digito verificador'
    if len(str(value)) < 7 or len(str(value)) > 8:
        raise ValidationError(error)
    
    value2 = str(value)
    
    for c in value2:
        if not c.isdigit():
            raise ValidationError(error)

def validar_nombre(value):
    error = 'Ingrese unicamente letras'
    
    for c in value:
        if not c.isalpha():
            raise ValidationError(error)
    


class Cliente(models.Model):
    rut = models.IntegerField(primary_key=True, validators=[validar_rut])
    
    DIGITO_VERIFICADOR = [
        ("1", "1"),
        ("2", "2"),
        ("3", "3"),
        ("4", "4"),
        ("5", "5"),
        ("6", "6"),
        ("7", "7"),
        ("8", "8"),
        ("9", "9"),
        ("K", "K"),
    ]
    dv = models.TextField(null=False, choices=DIGITO_VERIFICADOR)
    
    nombre = models.CharField(null=False, max_length=20, validators=[validar_nombre])
    apellido = models.CharField(null=False, max_length=20, validators=[validar_nombre])
    usuario = models.OneToOneField(User, on_delete=models.PROTECT)
    correo = models.EmailField(unique=True, null=False)
    
    def __str__(self):
        return str(f'{self.rut}')
