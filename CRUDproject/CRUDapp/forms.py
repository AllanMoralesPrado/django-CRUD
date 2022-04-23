from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext_lazy as _
from .models import Comuna,Region

class UserForm(UserCreationForm):
    first_name = forms.CharField()
    first_name.label = 'Nombre'
    last_name = forms.CharField()
    last_name.label = 'Apellido'
    email = forms.EmailField()
    email.label = 'Correo Electrónico'

    password1 = forms.CharField(label = 'Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label = 'Confirme contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('first_name','last_name','username','email','password1','password2')
        labels = {'username':_("Nombre de Usuario")}

class TipoForm(forms.Form):
    tipos = ((1, 'Arrendatario'),(2, 'Arrendador'),)
    tipo = forms.ChoiceField(choices=tipos)
    rut = forms.CharField(label='rut', max_length=100)
    direccion = forms.CharField(label='direccion', max_length=100)
    telefono = forms.CharField(label='telefono', max_length=100)

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','email']

class InmuebleForm(forms.Form):
    tipos = ((1,'Casa'),(2,'Departamento'),(3,'Parcela'),(4,'Estacionamiento'),(5,'Otro'))
    id_tipo_inmueble = forms.ChoiceField(choices=tipos)
    comunas = [(x.id,x.Comuna) for x in list(Comuna.objects.filter())]

    def nombre_comuna(e):
        return e[1]
    comunas.sort(key=nombre_comuna)

    id_comuna = forms.ChoiceField(choices=comunas)
    regiones = [(x.id,x.Region) for x in list(Region.objects.filter())]
    id_region = forms.ChoiceField(choices=regiones)
    nombre_inmueble = forms.CharField(label='Nombre Inmueble', max_length=100)
    descripcion = forms.CharField(label='Descripción del Inmueble', max_length=100)
    m2_construido = forms.CharField(label='M2 construidos', max_length=100)
    numero_banos = forms.CharField(label='Número de baños', max_length=100)
    numero_hab = forms.CharField(label='Número de habitaciones', max_length=100)
    direccion = forms.CharField(label='Dirección', max_length=100)
    m2_terreno = forms.CharField(label='M2 de terreno', max_length=100)
    numero_est = forms.CharField(label='Núm. de estacionamientos', max_length=100)
