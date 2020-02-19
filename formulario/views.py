from django.shortcuts import render,get_object_or_404, redirect
from .models import Cliente, Mascota, Paseador
from .forms import ClienteForm, MascotaFormm, PaseadorForm
from django.contrib import messages
from django.contrib.auth import authenticate


def Register_Cliente(request):
    form = ClienteForm()
    if request.method=="POST":
        form=ClienteForm(request.POST)
        if form.is_valid():
            form.save
            #form.cleaned_data
        #return redirect('register_cliente')
    else:
        form=ClienteForm()
    return render(request,'formulario.html',{'form':form})


def Register_mascota(request):
    if request.method=="POST":
        form=MascotaFormm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            #nombre = form.cleaned_data.get('nombre')
            #apellido = form.cleaned_data.get('apellido')
            #direccion = form.cleaned_data.get('direccion')
            #distrito = form.cleaned_data.get('distrito')
            #telefono = form.cleaned_data.get('telefono')
            #dni = form.cleaned_data.get('dni')
            #foto = form.cleaned_data.get('foto')
    else:
        form=MascotaFormm()
    return render(request,'formulario_mascota.html',{'form':form})


def Register_paseador(request):
    if request.method=="POST":
        form=PaseadorForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
    else:
        form=PaseadorForm()
    return render(request,'formulario_paseador.html',{'form':form})



# Create your views here.
