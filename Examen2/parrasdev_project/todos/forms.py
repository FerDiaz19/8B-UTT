from django import forms
from django.contrib.auth.models import User
from .models import Todo

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Contraseña',
        'class': 'form-control'
    }))

    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        labels = {
            'username': 'Nombre de usuario',
            'email': 'Correo electrónico',
        }
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Nombre de usuario', 'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Correo electrónico', 'class': 'form-control'}),
        }

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['title', 'is_done', 'user']
        labels = {
            'title': 'Título del pendiente',
            'is_done': '¿Está resuelto?',
            'user': 'Usuario asignado',
        }
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Escribe el título del pendiente', 'class': 'form-control'}),
            'is_done': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'user': forms.Select(attrs={'class': 'form-select'}),
        }
