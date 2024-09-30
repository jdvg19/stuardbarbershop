from django.shortcuts import render,redirect
from django.contrib import messages
from datetime import datetime
from Citas.models import Cita

def inicio(request):

    lista = Cita.objects.all().order_by('cita')

    return render(request,"Inicio/inicio.html",{'l':lista})


def reservado(request,id):
    Cita.objects.filter(id=id).update(estado=1)
    messages.success(request,f'Reserva Confirmada a las {datetime.today()}!')
    return redirect('Inicio')


def rechazar(request,id):
    Cita.objects.filter(id=id).update(estado=2)
    messages.error(request,f'Reserva Rechazada!')
    return redirect('Inicio')