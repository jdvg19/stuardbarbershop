from django.urls import path,include
from Productos import views


urlpatterns = [
   path('nuevo-producto/',views.nuevo,name="NuevoProducto"),
   path('listado-producto/',views.listado,name="ListadoProducto"),
   path('actualizar-producto/<int:id>',views.actualizar,name="UpdateProducto"),
   path('eliminar-producto/<int:id>',views.eliminar,name="DeleteProducto"),
]
