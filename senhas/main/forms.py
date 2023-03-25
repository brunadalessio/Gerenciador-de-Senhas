from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Senha
from django.contrib.auth.models import User

class RegistrarForm(UserCreationForm):
    email= forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'E-mail'}))
    username= forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Usuário'}))
    password1=forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', "placeholder": 'Senha', 'id':'password'}))
    password2=forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', "placeholder": 'Confirmar sua senha', 'id':'confirmPassword'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class LoginForm(AuthenticationForm):
    username= forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Usuário'}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', "placeholder": 'Senha', 'id':'password'}))


class SenhaForm(forms.ModelForm):
    categoria= forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Categoria (Facebook, Twitter...)', 'maxlength':'50'}))
    email= forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'E-mail da conta', 'maxlength':'320'}))
    senha=forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', "placeholder": 'Senha da conta', 'id':'password', 'maxlength':'127'}))

    class Meta:
        model = Senha
        fields = ['categoria', 'email', 'senha']