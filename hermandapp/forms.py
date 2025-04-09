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


class PapeletaForm(forms.ModelForm):
    class Meta:
        model = PapeletaSitio
        fields = ['codigo', 'tipo', 'hermano']


class TitularForm(forms.ModelForm):
    class Meta:
        model = Titular
        fields = ['nombre', 'descripcion', 'anyo', 'procesiona', 'autor', 'imagen']
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nombre del Titular',
                'id': 'nombre'
            }),
            'descripcion': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Información del Titular',
                'id': 'descripcion'
            }),
            'anyo': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Catalogado en el año',
                'id': 'anyo'
            })
        }

    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre')

        if len(nombre) < 10:
            self.add_error('nombre', 'El nombre tiene que contener al menos 10 caracteres')

        return nombre

    def clean_anyo(self):
        anyo = self.cleaned_data.get('anyo')
        if anyo < 1000:
            self.add_error('anyo', 'No se puede catalogar una imagen con más de 1000 años de antigüedad')

        return anyo