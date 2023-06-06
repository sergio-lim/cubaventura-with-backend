from django import forms
from .models import Contacto,Destino
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth.models import User
class ContactoForm(forms.ModelForm):
    
    class Meta:
        model = Contacto
        fields = '__all__'

class DestinoForm(forms.ModelForm):
    class Meta:
        model = Destino
        fields = '__all__'
        widgets = {
        "fecha":forms.SelectDateWidget()
        }
        
class authenticationForm(AuthenticationForm):
    pass

class userCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password1','password2','is_staff']

class userCreationFormN(UserCreationForm):

    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password1','password2']