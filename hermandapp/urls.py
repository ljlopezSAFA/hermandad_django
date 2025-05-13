from django.urls import path, include
from hermandapp.views import *

urlpatterns = [
    # URL , METODO , NOMBRE_ABREV
    path('', go_home, name='home'),
    path('home/', go_home, name='home_page'),
    path('aboutus/', go_about_us, name='about_us'),
    path('titulares/', go_titulares, name='titulares'),
    path('crear_titular/', crear_titular, name='generar_titular'),
    path('templo/', go_templo_page, name='templo'),
    path('hermanos/', cargar_listado_hermanos, name='hermanos'),
    path('cultos/', cargar_cultos, name='cultos'),
    path('cultos/crear', crear_culto, name='crear_culto'),
    path('hermanos/<int:id>', crear_editar, name='hermanos_gestion'),
    path('hermanos/delete/<int:id>', eliminar_hermano, name='eliminar_hermano'),
    path('composiciones_musicales/', go_composiciones, name='composiciones'),
    path('composiciones_musicales/new/<int:id>', new_composicion, name='new_composicion'),
    path('composiciones_musicales/eliminar/<int:id>', eliminar_composicion, name='eliminar'),
    path('crear_papeleta/', crear_o_editar_papeleta, name='crear_papeleta'),
    path('editar_papeleta/<int:id>/', crear_o_editar_papeleta, name='editar_papeleta'),
    path('eliminar_papelta/<int:id>/', eliminar_papeleta, name='eliminar_papeleta'),
    path('listar_papeletas/', listar_papeletas, name='papeletas'),
    path('junta_gobierno/', junta_gobierno, name='junta_gobierno'),
    path('tienda/', ir_tienda, name='tienda'),
    path('carrito/add/<int:id>/', add_carrito, name='add_carrito'),
    path('ver_carrito/', ver_carrito, name='ver_carrito'),
    path('carrito/sumar/<int:id>/', sumar_carrito, name='sumar_carrito'),
    path('carrito/restar/<int:id>/', restar_carrito, name='restar_carrito'),
    path('completar_compra/', comprar, name='comprar'),
    path('carrito/quitar/<int:id>/', quitar_de_carrito, name='quitar_de_carrito'),
    # URLS DE LOGIN Y REGISTRO
    path('registro/', registrar_usuario, name='registro'),
    path('login/', loguearse, name='login'),
    path('logout/', logout_usuario, name='logout'),

]
