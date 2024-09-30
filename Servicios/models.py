from django.db import models

class Servicios(models.Model):
    nombre = models.CharField(max_length=250,blank=False,null=False)
    tiempo = models.IntegerField(blank=False,null=False,default=0)
    precio = models.DecimalField(max_digits=4,decimal_places=2,blank=False,null=False,default=0.00)
    

    class Meta:
        ordering = ["id"]

    def __str__(self):
        return self.nombre