from django.shortcuts import render, redirect,get_object_or_404
from .models import Comentario, Blog, Categoria
from .forms import ComentarioForm, BlogForm, CategoriaForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required



def blog(request):
    blogs = Blog.objects.all()
    cat= Categoria.objects.all()
    data = {
        'blogs':blogs,
        'cat': cat
    }
    
    
    return render(request, 'blog/blog.html', data)



def gestionarC(request, blog_id):
    blog = Blog.objects.get(id=blog_id)
    return render(request, 'blog/gestionarC.html', {"blog":blog})

@login_required
def gestionarB(request):
    blogs = Blog.objects.all()
    data={
        'blog':blogs

    }
    
    return render(request, 'blog/gestionarB.html',data)

def gestionarCategoría(request):
    cat= Categoria.objects.all()
    data={
        'cat':cat
    }
    return render(request, 'blog/gestionarCate.html',data)


def crearcoment(request, pk):
    if request.method == "POST":
        contenido= request.POST[str(pk) + "-" + "comentario"]
        Comentario.objects.create(nombre=request.user, comentario=contenido, blog=get_object_or_404(Blog,pk=pk))
        return redirect("gestionarC", blog_id=pk)
    
def borrarcoment(request, pk_new, pk_comentario):
    blog=Blog.objects.get(id=pk_new)
    comentario= blog.comentario_set.get(id=pk_comentario)
    contenido = "\"El contenido de este mensaje ha sido censurado por ser de naturaleza ofensiva.\""
    if comentario.comentario == contenido:
        comentario.delete()
    else:
        comentario.comentario=contenido
        comentario.save()
    return redirect("gestionarC", blog.id)
    
def agregarB(request):
    data ={
        'form':BlogForm()
    }
    if request.method == 'POST':
        formulario = BlogForm(data = request.POST, files= request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Agregado con éxito")
        else:
            data["form"] = formulario
    return render(request, 'blog/agregarB.html',data)

def modificarB(request,id):
    # Destino().objects.get()
    blog = get_object_or_404(Blog, id = id)
    data ={
        'form': BlogForm(instance=blog)
    }
    if request.method == 'POST':
        formulario = BlogForm(data=request.POST, instance=blog, files= request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Modificado con éxito")
            return redirect(to="gestionarB")
        data["form"] = formulario
    return render(request, 'Blog/modificar.html',data)

def eliminarB(request,id):
    blog = get_object_or_404(Blog, id=id)
    blog.delete()
    messages.success(request, "Eliminado con éxito")
    return redirect(to="gestionarB")

def agregarCate(request):
    data ={
        'form':CategoriaForm()
    }
    if request.method == 'POST':
        formulario = CategoriaForm(data = request.POST, files= request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Agregado con éxito")
        else:
            data["form"] = formulario
    return render(request, 'blog/agregarCate.html',data)

def modificarCate(request,id):
    # Destino().objects.get()
    cat = get_object_or_404(Categoria, id = id)
    data ={
        'form': CategoriaForm(instance=cat)
    }
    if request.method == 'POST':
        formulario = CategoriaForm(data=request.POST, instance=cat, files= request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Modificado con éxito")
            return redirect(to="gestionarCate")
        data["form"] = formulario
    return render(request, 'Blog/modificarCate.html',data)

def eliminarCate(request,id):
    cat = get_object_or_404(Categoria, id=id)
    cat.delete()
    messages.success(request, "Eliminado con éxito")
    return redirect(to="gestionarCategoría")

def categoria(request,categoria_id):
    categoria=Categoria.objects.get(id=categoria_id)
    blog= Blog.objects.filter(categoria=categoria)
    cat= Categoria.objects.all()
    return render (request, 'Blog/categorias.html',{'categoria':categoria, 'blog':blog, 'cat':cat} )