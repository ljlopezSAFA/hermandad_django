from django import forms
from .models import Hermano


class HermanoForm(forms.ModelForm):
    class Meta:
        model = Hermano
        fields = ['nombre', 'apellidos', 'dni', 'mail', 'fecha_nacimiento']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre', 'id': 'inputnombre'}),
            'apellidos': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Apellidos', 'id': 'inputapellidos'}),
            'dni': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'DNI', 'id': 'inputdni'}),
            'mail': forms.EmailInput(
                attrs={'class': 'form-control', 'placeholder': 'Correo electrónico', 'id': 'floatingInput'}),
            'fecha_nacimiento': forms.DateInput(
                attrs={'class': 'form-control', 'type': 'date', 'id': 'inputfechaNacimiento'}),
        }
