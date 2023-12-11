# myapp/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .forms import ItemForm, RegistrationForm
from .models import Item
from django.contrib import messages

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('login')  # Redirige al formulario de inicio de sesión
    else:
        # Si es una solicitud GET, puedes manejarla de la manera que desees
        return redirect('home')  # Por ejemplo, podrías redirigir a la página de inicio

def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registration successful. Welcome!')
            return redirect('home')
        else:
            messages.error(request, 'Registration failed. Please correct the errors below.')
    else:
        form = RegistrationForm()
    
    return render(request, 'register.html', {'form': form})



def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


@login_required
def home(request):
    items = Item.objects.filter(user=request.user)
    return render(request, 'home.html', {'items': items})

@login_required
def item_create(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            item.user = request.user
            item.save()
            return redirect('home')
    else:
        form = ItemForm()
    return render(request, 'item_create.html', {'form': form})

@login_required
def item_update(request, item_id):
    item = Item.objects.get(id=item_id, user=request.user)
    if request.method == 'POST':
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ItemForm(instance=item)
    return render(request, 'item_update.html', {'form': form, 'item': item})

@login_required
def item_delete(request, item_id):
    item = Item.objects.get(id=item_id, user=request.user)
    item.delete()
    return redirect('home')

@login_required
def logout_view(request):
    logout(request)
    return redirect('login')
