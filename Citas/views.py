from django.shortcuts import render,redirect
from Citas.models import Cita
from Estilos.models import Estilos
from django.contrib import messages

def nueva(request):
    
    if request.method == "POST":
        
        c = Cita()
        c.cliente = request.POST['cliente']
        c.tel = request.POST['tel']
        c.cita = request.POST['cita']
        c.hora = request.POST['hora']
        c.servicio = request.POST['servicio']
        c.barbero = request.POST['barbero']
        c.save()
        messages.success(request,f'Cita Agregada para el dia {c.cita} a las {c.hora} hrs Espere Confirmacion!')
        return redirect('NuevaCita')

    return render(request,'Citas/nueva.html')

def listado(request):
    
    citas = Citas.objects.all()

    return render(request,'Citas/listado.html',{'citas':citas})

def actualizar(request,id):
    c = Citas.objects.get(id=id)

    if request.method == "POST":
        
        Citas.objects.filter(id=id).update(cliente=request.POST['cliente'],telefono=request.POST['tel'],cita=request.POST['cita'])
        messages.success(request,f'Citas {c.cliente} Actualizado!')
        return redirect('ListadoCitas')
    
    return render(request,'Citas/actualizar.html',{'c':c})

def eliminar(request,id):
    Citas.objects.filter(id=id).delete()
    messages.success(request,f'Cita Eliminada!')
    return redirect('ListadoCitas')