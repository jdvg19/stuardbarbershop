from django.shortcuts import render,redirect
from Citas.models import Cita
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
    
    cortes = Estilos.objects.all()

    return render(request,'Citas/listado.html',{'cortes':cortes})


def actualizar(request,id):
    e = Estilos.objects.get(id=id)

    if request.method == "POST":
        
        Estilos.objects.filter(id=id).update(nombre=request.POST['nombre'],descripcion=request.POST['descripcion'],foto=f"estilos/{request.FILES['foto']}")
        messages.success(request,f'Estilo {e.nombre} Actualizado!')
        return redirect('ListadoEstilo')
    
    return render(request,'Citas/actualizar.html',{'e':e})


def eliminar(request,id):
    Estilos.objects.filter(id=id).delete()
    messages.success(request,f'Estilo Eliminado!')
    return redirect('ListadoEstilo')