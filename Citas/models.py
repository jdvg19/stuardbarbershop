from django.db import models

class Cita(models.Model):
    cliente = models.CharField(max_length=250,blank=False,null=False,verbose_name="cliente")
    tel = models.CharField(max_length=8,blank=False,null=False,default=0,verbose_name="telefono")
    cita = models.DateField(blank=False,null=False,verbose_name="fecha")
    hora = models.TimeField(blank=False,null=False,verbose_name="hora")
    servicio = models.CharField(max_length=250,blank=False,null=False,verbose_name="servicio")
    barbero = models.CharField(max_length=200,blank=False,null=False,verbose_name="barbero")
    fecha_reserva = models.DateTimeField(blank=False,null=False,auto_now_add=True,verbose_name="fecha_reserva")
    estado = models.IntegerField(blank=False,null=False,default=0,verbose_name="estado")
    reserva_cita = models.CharField(max_length=50, blank=True,null=True,verbose_name="cita")

    class Meta:
       ordering = ["id"]

    def __str__(self):
        return self.cliente