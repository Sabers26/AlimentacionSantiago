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
        
        if formulario.is_valid():
            if User.objects.filter(username=usuario).exists():
                context = {
                'mensaje': '',
                'errores': {},
                'data': request.POST,
                'error_pass': '',
                'error_user': 'El usuario ingresado ya se encuentra registrado'
                }
                return render(request, 'app/registro/registro.html', context)
            else:
                if not password:
                    context = {
                    'mensaje': '',
                    'errores': {},
                    'data': request.POST,
                    'error_pass': 'Ingrese una contraseña',
                    'error_user': ''
                    }
                    return render(request, 'app/registro/registro.html', context)
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
                    
                    #return redirect('login')
                    context = {
                        'mensaje': 'cliente creado exitosamente',
                        'errores': {},
                        'data': {}
                    }
                    return render(request, 'app/registro/registro.html', context)
        else:
            error = formulario.errors.get_json_data()
            context = {
                'mensaje': '',
                'errores': error,
                'data': request.POST
            }
            return render(request, 'app/registro/registro.html', context)
    
    context = {
        'mensaje': '',
        'errores': {},
        'data': {}
    }
    return render(request, 'app/registro/registro.html', context)