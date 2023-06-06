from django.urls import path,include
from .views import home,contacto,gestionarD,agregarD,modificarD,eliminarD,destinos,register, user, eliminarUsuario, editarUsuario

urlpatterns = [
    path('', home, name="home"),
    path('administrar/gestionarD/', gestionarD, name="gestionarD"),
    path("administrar/gestionarD/agregarD/", agregarD, name="agregarD"),
    path("administrar/gestionarD/modificarD/<id>/", modificarD, name="modificarD"),
    path("administrar/gestionarD/eliminarD/<id>/", eliminarD, name="eliminarD"),
    path('contacto/',contacto, name="contacto"),
    path('destinos/',destinos, name="destinos"),
    path('Usuarios/', user, name="Usuarios"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('logout/', exit,name='Logout'),
    path('register/', register,name='register'),
    path('editarUsuario/', editarUsuario,name='editarUsuario'),
    path('eliminarUsuario/', eliminarUsuario, name="eliminarUsuario"),
]