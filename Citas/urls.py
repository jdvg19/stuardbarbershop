from django.urls import path,include
from Citas import views


urlpatterns = [
   path('nueva-cita/',views.nueva,name="NuevaCita"),
   path('listado-cita/',views.listado,name="ListadoCita"),
   path('actualizar-cita/<int:id>',views.actualizar,name="UpdateCita"),
   path('eliminar-cita/<int:id>',views.eliminar,name="DeleteCita"),
]
