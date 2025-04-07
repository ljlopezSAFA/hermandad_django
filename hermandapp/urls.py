from django.urls import path
from hermandapp.views import *

urlpatterns = [
    # URL , METODO , NOMBRE_ABREV
    path('', go_home, name='home'),
    path('home/', go_home, name='home_page'),
    path('aboutus/', go_about_us, name='about_us'),
    path('titulares/', go_titulares, name='titulares'),
    path('crear_titular/', crear_titular_default, name='generar_titular'),
    path('templo/', go_templo_page, name='templo'),
    path('hermanos/', cargar_listado_hermanos, name='hermanos'),
    path('hermanos/<int:id>', crear_editar, name='hermanos_gestion'),
    path('hermanos/delete/<int:id>', eliminar_hermano, name='eliminar_hermano'),
    path('composiciones_musicales/', go_composiciones, name='composiciones'),
    path('composiciones_musicales/new/<int:id>', new_composicion, name='new_composicion'),
    path('composiciones_musicales/eliminar/<int:id>', eliminar_composicion, name='eliminar'),
]
