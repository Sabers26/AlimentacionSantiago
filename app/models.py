from django.db import models
from django.core.validators import RegexValidator, MinLengthValidator, MinValueValidator, MaxLengthValidator, MaxValueValidator
from django.contrib.auth.models import User
# Create your models here.

#Validacion de solo letras. . . 


class Cliente(models.Model):
    rut = models.IntegerField(primary_key=True, validators=(MinLengthValidator(7), MaxLengthValidator(8)))
    
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
    
    nombre = models.TextField(null=False, validators=(MinLengthValidator(1), MaxLengthValidator(20)))
    apellido1 = models.TextField(null=False, validators=(MinLengthValidator(1), MaxLengthValidator(20)))
    apellido2 = models.TextField(null=False, validators=(MinLengthValidator(1), MaxLengthValidator(20)))
    Usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    correo = models.EmailField(unique=True, null=False)
    
    def __str__(self):
        return str(f'{self.rut}')
