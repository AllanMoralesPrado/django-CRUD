from django.shortcuts import render, redirect
from CRUDapp.models import *
from CRUDapp.forms import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

def registerView(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/register_tipo?user='+str(form.cleaned_data['username']))
    else:
        form = UserForm()
        
    return render(request,'registration/register.html',{'form':form})

def register_tipoView(request):
    username = request.GET['user']
    if request.method == 'POST':
        form = TipoForm(request.POST)
        if form.is_valid():
            form = TipoForm(request.POST)
            print(form)
            tipo = form.cleaned_data['tipo']
            rut = form.cleaned_data['rut']
            direccion = form.cleaned_data['direccion']
            telefono = form.cleaned_data['telefono']
            user = User.objects.filter(username=username)[0]
            tipo_user = Tipo_user.objects.filter(id=int(tipo))[0]
            datos = Profile(user=user,id_tipo_user=tipo_user,rut=rut,direccion=direccion,telefono=telefono)
            datos.save()
            return HttpResponseRedirect('/login/')
    else:
        form = TipoForm()
    return render(request,'registration/register_tipo.html',{'form':form})

@login_required
def dashboardView(request):
    return render(request,'dashboard.html', {})

def indexView(request):
    return render(request, 'index.html', {})

# Create your views here.
