from django.shortcuts import render,redirect
from Estilos.models import Estilos
from django.contrib import messages

def nuevo(request):
    
    if request.method == "POST":

        e = Estilos()
        e.nombre = request.POST['nombre']
        e.descripcion = request.POST['descripcion']
        e.foto = request.FILES['foto']
        e.save()
        messages.success(request,f'Estilo {e.nombre} Ingresado!')
        return redirect('NuevoEstilo')

    return render(request,'Estilos/nuevo.html')

def listado(request):
    
    cortes = Estilos.objects.all()

    return render(request,'Estilos/listado.html',{'cortes':cortes})

def actualizar(request,id):
    e = Estilos.objects.get(id=id)

    if request.method == "POST":
        
        Estilos.objects.filter(id=id).update(nombre=request.POST['nombre'],
        descripcion=request.POST['descripcion'],foto=f"estilos/{request.FILES['foto']}")
        messages.success(request,f'Estilo {e.nombre} Actualizado!')
        return redirect('ListadoEstilo')
    
    return render(request,'Estilos/actualizar.html',{'e':e})

def eliminar(request,id):
    Estilos.objects.filter(id=id).delete()
    messages.success(request,f'Estilo Eliminado!')
    return redirect('ListadoEstilo')