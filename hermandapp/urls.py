from django.urls import path
from hermandapp.views import *

urlpatterns = [
    # URL , METODO , NOMBRE_ABREV
    path('', go_home, name='home'),
    path('home/', go_home, name='home_page'),
    path('aboutus/', go_about_us, name='about_us'),
    path('titulares/', go_titulares, name='titulares'),
    path('crear_titular/', crear_titular_default, name='generar_titular'),
    path('templo/', go_templo_page , name='templo'),
    path('hermanos/', cargar_listado_hermanos, name='hermanos'),
]
