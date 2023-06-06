from django import forms
from Blog.models import Comentario, Blog, Categoria



class ComentarioForm(forms.ModelForm):
    class Meta:
        models = Comentario
        fields = ['nombre','correo','destino','comentario']
        
class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = '__all__'
        widgets = {
        "fecha":forms.SelectDateWidget()
        }

class CategoriaForm(forms.ModelForm):
    class Meta:
        model =Categoria
        fields='__all__'
        widgets = {
        "fecha":forms.SelectDateWidget()
        }

        