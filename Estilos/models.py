from django.db import models

class Estilos(models.Model):
    nombre = models.CharField(max_length=250,blank=False,null=False)
    descripcion = models.CharField(max_length=250,blank=False,null=False)
    foto = models.ImageField(upload_to='estilos/',blank=True,null=True,default='S/F')
    fecha = models.DateField(blank=False,null=False,auto_now_add=True)


    class Meta:
        ordering = ["id"]

    def __str__(self):
        return self.nombre