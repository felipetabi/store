from django.shortcuts import render, redirect

from django.contrib import messages
from django.contrib.auth import login, authenticate, logout

from .forms import RegisterForm

def index(request):
    return render(request,'index.html', {
        'message': 'Listado de Productos',
        'title': 'Productos',
        'products':[
            {'title': 'Playera', 'price': 5, 'stock': True},
            {'title': 'Camisa', 'price': 7, 'stock': True},
            {'title': 'Mochila', 'price': 20, 'stock': False},
            {'title': 'Laptop', 'price': 520, 'stock': False},
        ]        
    })

def login_view(request):
    if request.method =='POST':
        username = request.POST.get('username') #DICCIONARIO 
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)#none
        if user:
            login(request, user)
            messages.success(request, 'Bienvenido {}'.format(user.username))
            return redirect('index')
        else:
            messages.error(request, 'Usuario y contraseña no validos')

    return render(request, 'users/login.html', {
         
    })

def logout_view(request):
    logout(request)
    messages.success(request, 'Sesión cerrada exitosamente')
    return redirect('login')

def register(request):
    form = RegisterForm()
    return render(request, 'users/register.html', {
        'form': form
    })