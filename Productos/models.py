from django.db import models

class Productos(models.Model):
    nombre = models.CharField(max_length=250,blank=False,null=False)
    descripcion = models.CharField(max_length=250,blank=False,null=False)
    precio = models.DecimalField(max_digits=4,decimal_places=2,blank=False,null=False,default=0.00)
    foto = models.ImageField(upload_to='productos/',blank=True,null=True,default='S/F')
    


    class Meta:
        ordering = ["id"]

    def __str__(self):
        return self.nombre