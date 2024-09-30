from django.urls import path,include
from Login import views

urlpatterns = [
   path('',views.login,name="Login")
]
