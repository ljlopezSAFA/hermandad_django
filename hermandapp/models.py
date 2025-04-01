from django.db import models


# Create your models here.
class Titular(models.Model):
    nombre= models.CharField(max_length=250)
    descripcion = models.TextField()
    anyo= models.IntegerField()
    procesiona = models.BooleanField(default=True)
    imagen = models.CharField(max_length=1000)
    autor= models.CharField(max_length=250)

    def __str__(self):
        return self.nombre


class Hermano(models.Model):
    nombre = models.CharField(max_length=250)
    apellidos = models.CharField(max_length=250)
    dni = models.CharField(max_length=9)
    mail = models.EmailField()
    fecha_nacimiento = models.DateTimeField()

    def __str__(self):
        return self.nombre








# class Titular(models.Model):
#     nombre = models.CharField(max_length=250)
#     descripcion = models.TextField()
#     autor = models.CharField(max_length=250)
#     anyo = models.IntegerField()
#     imagen = models.CharField(max_length=1000)
#     procesiona = models.BooleanField(default=False)
#
#     def __str__(self):
#         return self.nombre


