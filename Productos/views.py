from django.shortcuts import render,redirect
from Productos.models import Productos
from django.contrib import messages


def nuevo(request):
    
    if request.method == "POST":

        p = Productos()
        p.nombre = request.POST['nombre']
        p.descripcion = request.POST['descripcion']
        p.precio = request.POST['precio']
        p.foto = request.FILES['foto']
        p.save()
        messages.success(request,f'Producto {p.nombre} Ingresado!')
        return redirect('NuevoProducto')

    return render(request,'Productos/nuevo.html')



def listado(request):
    
    productos = Productos.objects.all()

    return render(request,'Productos/listado.html',{'productos':productos})


def actualizar(request,id):
    p = Productos.objects.get(id=id)

    if request.method == "POST":
        
        Productos.objects.filter(id=id).update(nombre=request.POST['nombre'],descripcion=request.POST['descripcion'],foto=f"productos/{request.FILES['foto']}")
        messages.success(request,f'Producto {p.nombre} Actualizado!')
        return redirect('ListadoProducto')
    
    return render(request,'Productos/actualizar.html',{'p':p})


def eliminar(request,id):
    Productos.objects.filter(id=id).delete()
    messages.success(request,f'Producto Eliminado!')
    return redirect('ListadoProducto')