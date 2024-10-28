from django.shortcuts import render,redirect
from Servicios.models import Servicios
from django.contrib import messages
from django.contrib.auth.decorators import login_required


@login_required
def nuevo(request):
    
    if request.method == "POST":

        s = Servicios()
        s.nombre = request.POST['nombre']
        s.tiempo = request.POST['tiempo']
        s.precio = request.POST['precio']
        s.save()
        messages.success(request,f'Servicio {s.nombre} Ingresado!')
        return redirect('NuevoServicio')

    return render(request,'Servicios/nuevo.html')


@login_required
def listado(request):
    
    servicios = Servicios.objects.all()

    return render(request,'Servicios/listado.html',{'servicios':servicios})


@login_required
def actualizar(request,id):
    s = Servicios.objects.get(id=id)

    if request.method == "POST":
        
        Servicios.objects.filter(id=id).update(nombre=request.POST['nombre'],tiempo=request.POST['tiempo'],precio=request.POST['precio'])
        messages.success(request,f'Servicio {s.nombre} Actualizado!')
        return redirect('ListadoServicio')
    
    return render(request,'Servicios/actualizar.html',{'s':s})


@login_required
def eliminar(request,id):
    
    Servicios.objects.filter(id=id).delete()
    messages.success(request,f'Servicio Eliminado!')
    return redirect('ListadoServicio')