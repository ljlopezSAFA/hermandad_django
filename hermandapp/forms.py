from django import forms
from .models import *


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
                attrs={'class': 'form-control', 'type': 'date-local', 'id': 'inputfechaNacimiento'}),
        }


class CultoForm(forms.ModelForm):
    class Meta:
        model = Culto
        fields = ['nombre', 'descripcion', 'fecha_inicio', 'fecha_fin', 'titular', 'tipo']
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nombre del culto',
                'id': 'inputNombreCulto'
            }),
            'descripcion': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Descripción del culto',
                'id': 'inputDescripcion'
            }),
            'fecha_inicio': forms.DateTimeInput(attrs={
                'class': 'form-control',
                'type': 'datetime-local',
                'id': 'inputFechaInicio'
            }),
            'fecha_fin': forms.DateTimeInput(attrs={
                'class': 'form-control',
                'type': 'datetime-local',
                'id': 'inputFechaFin'
            }),
            'titular': forms.Select(attrs={
                'class': 'form-select',
                'id': 'inputTitular'
            }),
            'tipo': forms.Select(attrs={
                'class': 'form-select',
                'id': 'inputTipoCulto'
            }),
        }
