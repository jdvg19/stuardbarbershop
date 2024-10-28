from django.urls import path,include
from Login import views

urlpatterns = [
   path('',views.login_in,name="Login"),
   path('logout/',views.logout_out,name='Salir'),

]
