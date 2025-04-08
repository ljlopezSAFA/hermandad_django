from django.db import models


class TipoCulto(models.TextChoices):
    TRIDUO = 'TRIDUO', 'Triduo'
    QUINARIO = 'QUINARIO', 'Quinario'
    ROSARIO = 'ROSARIO', 'Rosario'
    VIA_CRUCIS = 'VIA_CRUCIS', 'Vía Crucis'
    VENERACION = 'VENERACION', 'Veneración'
    FUNCION_PRINCIPAL = 'FUNCION_PRINCIPAL', 'Función Principal'



class TipoPapeleta(models.TextChoices):
    NAZARENO = 'NAZARENO', 'Nazareno'
    MUSICO = 'MUSICO', 'Músico'
    GENERAL = 'GENERAL' 'General'



# Create your models here.
class Titular(models.Model):
    nombre = models.CharField(max_length=250)
    descripcion = models.TextField()
    anyo = models.IntegerField()
    procesiona = models.BooleanField(default=True)
    imagen = models.CharField(max_length=1000)
    autor = models.CharField(max_length=250, default='')

    def __str__(self):
        return self.nombre


class Hermano(models.Model):
    nombre = models.CharField(max_length=250)
    apellidos = models.CharField(max_length=250)
    dni = models.CharField(max_length=9)
    mail = models.EmailField()
    fecha_nacimiento = models.DateTimeField()
    telefono = models.CharField(max_length=15, null=True)

    def __str__(self):
        return self.nombre


class ComposicionMusical(models.Model):
    nombre = models.CharField(max_length=200)
    autor = models.CharField(max_length=150)
    fecha_creacion = models.DateField()
    es_marcha_procesional = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre


class Culto(models.Model):
    nombre = models.CharField(max_length=250)
    descripcion = models.TextField()
    fecha_inicio = models.DateTimeField()
    fecha_fin = models.DateTimeField()

    # Datos de la relación
    titular = models.ForeignKey(
        'Titular',  # modelo al que se relaciona
        on_delete=models.CASCADE,  # qué hacer si se borra el titular
        related_name='cultos'  # nombre para acceder desde el lado de Titular
    )

    tipo = models.CharField(
        max_length=30,
        choices=TipoCulto.choices,
        default=TipoCulto.FUNCION_PRINCIPAL
    )

    def __str__(self):
        return self.nombre



class PapeletaSitio(models.Model):
    codigo=models.CharField(max_length=15)
    tipo= models.CharField(
        max_length=50,
        choices= TipoPapeleta.choices,
        default= TipoPapeleta.GENERAL
    )
    hermano = models.ForeignKey(
        'Hermano',
        on_delete=models.DO_NOTHING,
        related_name= 'papeletas'
    )




















# class PapeletaSitio(models.Model):
#     codigo = models.CharField(max_length=15)
#
#     tipo = models.CharField(
#         max_length=40,
#         choices=TipoPapelta.choices,
#         default=TipoPapelta.GENERICA
#     )
#
#     hermano = models.ForeignKey(
#         'Hermano',
#         on_delete= models.DO_NOTHING,
#         related_name='papeletas'
#     )
#
#     def __str__(self):
#         return self.codigo + self.hermano.nombre + self.hermano.dni



