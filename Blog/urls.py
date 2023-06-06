from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('blog/',blog,name="blog"),
    path('blog/gestionarB.html/', gestionarB, name="gestionarB"),
    path("blog/gestionarB/agregarB/", agregarB, name="agregarB"),
    path("Blog/gestionarB/modificarB/<id>/", modificarB, name="modificarB"),
    path("Blog/gestionarB/eliminarB/<id>/", eliminarB, name="eliminarB"),
    path('blog/gestionarC.html/<blog_id>', gestionarC, name="gestionarC"),
    path('crear_comentario/<int:pk>', crearcoment, name="crearcoment"),
    path('eliminar_comentario/<int:pk_new>/<int:pk_comentario>/', borrarcoment, name="borrarcoment"),
    path('blog/gestionarCate.html/', gestionarCategoría, name="gestionarCategoría"),
    path("blog/gestionarCate/agregarCate/", agregarCate, name="agregarCate"),
    path("Blog/gestionarCate/modificarCate/<id>/", modificarCate, name="modificarCate"),
    path("Blog/gestionarCate/eliminarCate/<id>/", eliminarCate, name="eliminarCate"),
    path("categoria/<int:categoria_id>/",categoria, name='categoria' ),
    
]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)