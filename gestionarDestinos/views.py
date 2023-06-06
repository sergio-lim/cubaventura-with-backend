from django.shortcuts import render,redirect,get_object_or_404
from .models import Destino,Contacto
from .forms import ContactoForm,DestinoForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import logout
from .forms import userCreationForm,userCreationFormN,User
# Create your views here.
def home(request):
    return render(request, 'gestionarDestinos/home.html')
@login_required
@permission_required('gestionarDestinos.add_destino')
def gestionarD(request):
    destinos = Destino.objects.all()
    data={
        'destinos':destinos
    }
    return render(request, 'gestionarDestinos/destino/listar.html',data)
@login_required
@permission_required('gestionarDestinos.add_destino')
def agregarD(request):
    data ={
        'form':DestinoForm()
    }
    if request.method == 'POST':
        formulario = DestinoForm(data = request.POST, files= request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Agregado Con Exito")
        else:
            data["form"] = formulario
    return render(request, 'gestionarDestinos/destino/agregar.html',data)
@login_required
@permission_required('gestionarDestinos.add_destino')
def modificarD(request,id):
    # Destino().objects.get()
    destino = get_object_or_404(Destino, id = id)
    data ={
        'form': DestinoForm(instance=destino)
    }
    if request.method == 'POST':
        formulario = DestinoForm(data=request.POST, instance=destino, files= request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Modificado Con Exito")
            return redirect(to="gestionarD")
        data["form"] = formulario
    return render(request, 'gestionarDestinos/destino/modificar.html',data)
@login_required
@permission_required('gestionarDestinos.add_destino')
def eliminarD(request,id):
    destino = get_object_or_404(Destino, id=id)
    destino.delete()
    messages.success(request, "Eliminado Con exito")
    return redirect(to="gestionarD")

def contacto(request):
    data = {
        'form':ContactoForm()
    }
    if request.method == 'POST':
        formulario = ContactoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Mensaje Enviado")
        else:
            data["form"] = formulario

    return render(request, 'gestionarDestinos/contacto.html', data)


def destinos(request):
    destinos = Destino.objects.all()
    data={
        'destinos':destinos
    }
    return render(request, 'gestionarDestinos/destinos.html',data)


def register(request):

    if request.method == 'POST':
        formCreateUser = userCreationForm(data=request.POST)
        if formCreateUser.is_valid():
            formCreateUser.save()
            return redirect("home")

        formCreateUser1 = userCreationFormN(data=request.POST)
        if formCreateUser1.is_valid():
            formCreateUser1.save()
            return redirect("home")    

    return render(request,"registration/register.html",{"formR":userCreationForm,"formRN":userCreationFormN})

def exit(request):
    logout(request)
    return redirect('home')
@login_required
def user(request):
     usuarios=User.objects.all()
     print(usuarios[0].password)
     return render(request, 'gestionarDestinos/Usuarios.html',{"User": usuarios})

@login_required
def eliminarUsuario(request):
    
     idUser = request.GET.get("usuarioID","")

     if idUser != "":
            id = int(idUser)
            datoEliminar = User.objects.get(id=id)
            datoEliminar.delete()
     return redirect('/')
@login_required
def editarUsuario(request):
      
       newPassword = request.POST['contraE']
      
       idU = request.POST.get("usuarioID","")
       
       if idU != "":
            id = int(idU)
            newUser=User.objects.get(id=id)
          
            if newPassword != "":
             newUser.set_password(newPassword)
             
            newUser.save()
       return redirect('/')