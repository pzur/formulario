from django.forms import ModelForm
from django import forms
from .models import Cliente, Mascota, Paseador

class ClienteForm(forms.ModelForm):
    nombre = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Nombre'}))
    apellido = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Apellido'}))
    dni = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'DNI'}))
    telefono = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Telefono'}))
    direccion = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Direccion'}))
    distrito = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Distrito'}))
    foto = forms.CharField(widget=forms.FileInput(attrs={'placeholder':'Foto'}))
   
    
    class Meta:
        model = Cliente
        fields = '__all__'


class MascotaFormm(forms.ModelForm):
    nombre = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Nombre'}))
    tipo = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Tipo'}))
    raza = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Raza'}))
    años = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Años'}))
    sexo = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Sexo'}))
    alergia = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Alergia'}))
    foto = forms.CharField(widget=forms.FileInput(attrs={'placeholder':'Foto'}))

    class Meta:
        model = Mascota
        fields = '__all__'

class PaseadorForm(forms.ModelForm):
    nombre = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Nombre'}))
    apellido = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Apellido'}))
    dni = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'DNI'}))
    telefono = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Telefono'}))
    direccion = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Direccion'}))
    distrito = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Distrito'}))
    experiencia = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Experiencia'}))
    edad = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Edad'}))
    foto = forms.CharField(widget=forms.FileInput(attrs={'placeholder':'Foto'}))


    class Meta:
        model = Paseador
        fields = '__all__'
