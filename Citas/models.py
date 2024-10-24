from django.db import models

class Cita(models.Model):
    cliente = models.CharField(max_length=250,blank=False,null=False)
    tel = models.CharField(max_length=8,blank=False,null=False,default=0)
    cita = models.DateField(blank=False,null=False)
    hora = models.TimeField(blank=False,null=False)
    servicio = models.CharField(max_length=250,blank=False,null=False)
    barbero = models.CharField(max_length=200,blank=False,null=False)
    fecha_reserva = models.DateTimeField(blank=False,null=False,auto_now_add=True)
    estado = models.IntegerField(blank=False,null=False,default=0)
    reserva_cita = models.CharField(max_length=50, blank=True,null=True)

    class Meta:
       ordering = ["id"]

    def __str__(self):
        return self.cliente