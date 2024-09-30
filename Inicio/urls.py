from django.urls import path,include
from Inicio import views

urlpatterns = [
   path('',views.inicio,name="Inicio"),
   path('reservado/<int:id>',views.reservado,name="Confirmar"),
   path('rechazar/<int:id>',views.rechazar,name="Rechazar")
]
