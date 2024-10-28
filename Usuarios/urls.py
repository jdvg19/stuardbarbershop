from Usuarios import views
from django.urls import path
from django.conf import settings  # para agregar la ruta de la imagen
from django.conf.urls.static import static  # para agregar la ruta de la imagen

urlpatterns = [
    path('nuevousuario/', views.nuevoUsuario, name="NuevoUser"),
    path('listausuario/', views.listaUsuario, name="ListaUser"),
    path('updateusuario/<str:id>', views.updateUsuario, name="UpdateUser"),
    path('deleteusuario/<str:id>', views.deleteUsuario, name="DeleteUser"),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)