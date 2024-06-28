from django import forms
from .models import Contacto
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ContactoForm(forms.ModelForm):

    class Meta: 
        model = Contacto
        fields = ["nombre","correo","tipo_consulta", "mensaje", "aviso"]


class CustomeUserCreationForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ["username","first_name","last_name","email","password1","password2"]