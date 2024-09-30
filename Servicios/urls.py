from django.urls import path,include
from Servicios import views


urlpatterns = [
   path('nuevo-servicio/',views.nuevo,name="NuevoServicio"),
   path('listado-servicio/',views.listado,name="ListadoServicio"),
   path('actualizar-servicio/<int:id>',views.actualizar,name="UpdateServicio"),
   path('eliminar-servicio/<int:id>',views.eliminar,name="DeleteServicio"),
]
