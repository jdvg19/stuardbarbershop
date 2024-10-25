from django.urls import path,include
from Reportes import views


urlpatterns = [
   path('reporte/',views.reportepdf,name="Reporte"),
]
