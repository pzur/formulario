from django.shortcuts import render,get_object_or_404
from .models import Cliente, Mascota, Paseador
from .forms import ClienteForm, MascotaFormm, PaseadorForm


def Register_Cliente(request):
    if request.method=="POST":
        form=ClienteForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
    else:
        form=ClienteForm()
    return render(request,'formulario.html',{'form':form})

def Register_mascota(request):
    if request.method=="POST":
        form=MascotaFormm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
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
