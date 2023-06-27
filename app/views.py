from django.shortcuts import render, redirect
from .forms import RegistroForm
from . import models
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate

# Create your views here.


#Vista de registro de cuenta de usuario
def registro(request):
    
    if request.method == 'POST':
        rut = request.POST['rut']
        dv = request.POST['dv']
        nombre = request.POST['nombre']
        apellido = request.POST['apellido']
        usuario = request.POST['usuario']
        password = request.POST['password']
        correo = request.POST['correo']
        
        data = {
            'rut': rut,
            'dv': dv,
            'nombre': nombre, 
            'apellido': apellido,
            'correo': correo
        }
        
        formulario = RegistroForm(data=data)
        
        if formulario.is_valid:
            
            if not password:
                formulario.add_error('password', 'Agregue una contraseña')
            else:
                usr = User()
                usr.username = usuario
                usr.set_password(password)
                
                usr.save()
                
                cliente = formulario.save(commit=False)
                cliente.rut = rut
                cliente.dv = dv
                cliente.nombre = nombre
                cliente.apellido = apellido
                cliente.usuario = usr
                cliente.correo = correo
                cliente.save()
                
                return redirect('login')
    
    return render(request, 'app/registro/registro.html')