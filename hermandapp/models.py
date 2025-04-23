from datetime import datetime
from django.utils import timezone
from django.db import models
from datetime import timedelta
from dateutil.relativedelta import relativedelta  # mejor para años
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager,PermissionsMixin


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

class CargoHermandad(models.TextChoices):
    HERMANO_MAYOR = 'HERMANO_MAYOR', 'Hermano Mayor'
    TENIENTE_HERMANO_MAYOR = 'TENIENTE_HERMANO_MAYOR', 'Teniente Hno. Mayor'
    PROMOTORA_SACRAMENTAL = 'PROMOTORA_SACRAMENTAL', 'Promotora Sacramental'
    CONSILIARIO_PRIMERO = 'CONSILIARIO_PRIMERO', 'Consiliario Primero'
    CONSILIARIO_SEGUNDO = 'CONSILIARIO_SEGUNDO', 'Consiliario Segundo'
    FISCAL_PRIMERO = 'FISCAL_PRIMERO', 'Fiscal Primero'
    FISCAL_SEGUNDA = 'FISCAL_SEGUNDA', 'Fiscal Segunda'
    MAYORDOMO_PRIMERO = 'MAYORDOMO_PRIMERO', 'Mayordomo Primero'
    MAYORDOMO_SEGUNDO = 'MAYORDOMO_SEGUNDO', 'Mayordomo Segundo'
    SECRETARIO_PRIMERO = 'SECRETARIO_PRIMERO', 'Secretario Primero'
    SECRETARIO_SEGUNDO = 'SECRETARIO_SEGUNDO', 'Secretario Segundo'
    ARCHIVERO = 'ARCHIVERO', 'Archivero'
    PRIOSTE_PRIMERO = 'PRIOSTE_PRIMERO', 'Prioste Primero'
    PRIOSTE_SEGUNDO = 'PRIOSTE_SEGUNDO', 'Prioste Segundo'
    DIPUTADO_CARIDAD = 'DIPUTADO_CARIDAD', 'Diputado de Caridad'
    DIPUTADO_FORMACION = 'DIPUTADO_FORMACION', 'Diputado de Formación'
    DIPUTADO_MAYOR_GOBIERNO = 'DIPUTADO_MAYOR_GOBIERNO', 'Diputado Mayor de Gobierno'


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
        return self.apellidos +  " , " + self.nombre


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

def anio_actual():
    return datetime.now().year


class PapeletaSitio(models.Model):
    codigo = models.CharField(max_length=15)
    fecha_obtencion = models.DateTimeField(default=timezone.now)
    anyo = models.IntegerField(default=anio_actual)
    tipo = models.CharField(
        max_length=50,
        choices=TipoPapeleta.choices,
        default=TipoPapeleta.GENERAL
    )
    hermano = models.ForeignKey(
        'Hermano',
        on_delete=models.DO_NOTHING,
        related_name='papeletas'
    )

    @property
    def generar_codigo(self):
        ultimo = PapeletaSitio.objects.order_by('id').last()
        ultimo_id = ultimo.id if ultimo else 0
        return f"CP{self.anyo}{ultimo_id + 1}"

def fecha_fin_default():
    return timezone.now().date() + relativedelta(years=4)

class JuntaGobierno(models.Model):
    fecha_inicio = models.DateField(default=timezone.now)
    fecha_fin = models.DateField(default=fecha_fin_default)

    def __str__(self):
        return f"Junta desde {self.fecha_inicio} hasta {self.fecha_fin}"

class MiembroJunta(models.Model):
    junta_gobierno = models.ForeignKey('JuntaGobierno', on_delete=models.CASCADE, related_name='miembros')
    cargo = models.CharField(max_length=80, choices=CargoHermandad.choices)

    def __str__(self):
        return self.junta_gobierno.id + self.cargo.lower()



#LOGIN Y REGISTRO
class UsuarioManager(BaseUserManager):

    def create_user(self, email, nombre, rol, password=None):
        if not email:
            raise ValueError("El usuario debe tener un email")
        email = self.normalize_email(email)
        usuario = self.model(email=email, nombre=nombre, rol=rol)
        usuario.set_password(password)
        usuario.save(using=self._db)
        return usuario

    def create_superuser(self, email, nombre, rol='admin', password=None):
        usuario = self.create_user(email, nombre, rol, password)
        usuario.is_superuser = True
        usuario.is_staff = True
        usuario.save(using=self._db)
        return usuario



class Usuario(AbstractBaseUser, PermissionsMixin):
    ROLES = (
        ('admin', 'Administrador'),
        ('hermano', 'Hermano'),
        ('gestor', 'Gestor'),
        ('miembro_junta', 'MiembroJunto')
    )

    email = models.EmailField(max_length=500, unique=True)
    nombre = models.CharField(max_length=250)
    rol = models.CharField(max_length=25,choices=ROLES)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UsuarioManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nombre', 'rol']

    def __str__(self):
        return self.email + "-" + self.nombre + ":"+ self.rol






