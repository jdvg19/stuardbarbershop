from django.urls import path,include
from Estilos import views


urlpatterns = [
   path('nuevo-estilo/',views.nuevo,name="NuevoEstilo"),
   path('listado-estilo/',views.listado,name="ListadoEstilo"),
   path('actualizar-estilo/<int:id>',views.actualizar,name="UpdateEstilo"),
   path('eliminar-estilo/<int:id>',views.eliminar,name="DeleteEstilo"),
]
