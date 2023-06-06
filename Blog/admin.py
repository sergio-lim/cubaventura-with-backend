from django.contrib import admin
from .models import Comentario
from .models import Blog, Categoria
admin.site.register(Comentario)
admin.site.register(Blog)
admin.site.register(Categoria)
