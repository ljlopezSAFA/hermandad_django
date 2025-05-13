from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.exceptions import PermissionDenied
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404

from hermandapp.forms import *
from hermandapp.models import *


def es_admin(user):
    if not user.is_authenticated or not user.rol == 'admin':
        raise PermissionDenied
    return True


def es_gestor(user):
    if not user.is_authenticated or not user.rol == 'gestor':
        raise PermissionDenied
    return True


@login_required
def go_home(request):
    return render(request, 'home.html')


def go_about_us(request):
    return render(request, 'about_us.html')


@login_required
def go_templo_page(request):
    return render(request, 'templo.html')


def cargar_listado_hermanos(request):
    busqueda = request.GET.get('busqueda', '')
    hermanos_qs = Hermano.objects.all()

    if busqueda:
        hermanos_qs = hermanos_qs.filter(
            Q(nombre__icontains=busqueda) |
            Q(apellidos__icontains=busqueda) |
            Q(dni__icontains=busqueda) |
            Q(mail__icontains=busqueda) |
            Q(telefono__icontains=busqueda)
        )

    # Paginación
    paginator = Paginator(hermanos_qs.order_by('apellidos'), 10)  # 10 hermanos por página
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'hermanos.html', {
        'hermanos': page_obj,  # esto es un Page object
        'busqueda': busqueda,  # para mantener el valor en el input
    })


def cargar_cultos(request):
    cultos = Culto.objects.all()
    return render(request, 'cultos.html', {'cultos': cultos})


def formulario_hermano(request):
    return render(request, 'formulario_hermanos.html')


def go_titulares(request):
    list_titulares = Titular.objects.all()
    return render(request, 'titulares.html', {'titulares': list_titulares})


def go_composiciones(request):
    lista_composiciones = ComposicionMusical.objects.all()
    return render(request, 'composiciones.html', {'composiciones': lista_composiciones})


def new_composicion(request, id):
    composicion = ComposicionMusical.objects.filter(id=id)

    if len(composicion) == 0:
        composicion_nueva = ComposicionMusical()
    else:
        composicion_nueva = composicion[0]

    if request.method == 'POST':
        # RECOGER LOS DATOS
        composicion_nueva.nombre = request.POST['nombre']
        composicion_nueva.autor = request.POST['autor_de_composicion']
        composicion_nueva.fecha_creacion = request.POST['fecha']
        composicion_nueva.es_marcha_procesional = True

        # GUARDAR EN BASE DE DATOS
        composicion_nueva.save()

        # REDIRIGIR AL USUARIO A LA Página de listar
        return redirect('composiciones')


    else:
        return render(request, 'formulario_composicion.html', {'composicion': composicion_nueva})


def eliminar_composicion(request, id):
    composicion_eleminar = ComposicionMusical.objects.filter(id=id)

    if len(composicion_eleminar) != 0:
        composicion_eleminar[0].delete()

    return redirect('composiciones')


@user_passes_test(es_admin)
def crear_editar(request, id):
    if id != 0:
        hermano = get_object_or_404(Hermano, id=id)  # Si existe, lo obtenemos
    else:
        hermano = None  # Si no, es un nuevo hermano

    if request.method == "POST":
        form = HermanoForm(request.POST, instance=hermano)
        if form.is_valid():
            form.save()
            return redirect('hermanos')  # Cambia a la vista que prefieras
        else:
            return render(request, 'formulario_hermanos.html', {'form': form})
    else:
        form = HermanoForm(instance=hermano)

    return render(request, 'formulario_hermanos.html', {'form': form})


@user_passes_test(es_admin)
def eliminar_hermano(request, id):
    hermano = get_object_or_404(Hermano, id=id)  # Si existe, lo obtenemos

    if hermano:
        hermano.delete()

    return redirect('hermanos')


def eliminar_papeleta(request, id):
    papeleta = get_object_or_404(PapeletaSitio, id=id)  # Si existe, lo obtenemos

    if papeleta:
        papeleta.delete()

    return redirect('papeletas')


# Crear culto
def crear_culto(request):
    if request.method == 'POST':
        form = CultoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cultos')  # Asegúrate de tener esta URL configurada
    else:
        form = CultoForm()

    return render(request, 'formulario_cultos.html', {'form': form})


# Editar culto
def editar_culto(request, culto_id):
    culto = get_object_or_404(Culto, id=culto_id)

    if request.method == 'POST':
        form = CultoForm(request.POST, instance=culto)
        if form.is_valid():
            form.save()
            return redirect('lista_cultos')
    else:
        form = CultoForm(instance=culto)

    return render(request, 'formulario_cultos.html', {'form': form})


def listar_papeletas(request):
    # Obtener todas las papeletas de sitio
    papeletas = PapeletaSitio.objects.all()

    return render(request, 'papeletas.html', {
        'papeletas': papeletas
    })


def junta_gobierno(request):
    junta_gobierno = JuntaGobierno.objects.all()

    return render(request, 'junta_gobierno.html', {
        'junta': junta_gobierno
    })


@user_passes_test(es_admin)
def crear_o_editar_papeleta(request, id=None):
    if id:
        papeleta = get_object_or_404(PapeletaSitio, id=id)
    else:
        # Creamos la papeleta pero sin guardarla aún
        papeleta = PapeletaSitio()
        papeleta.codigo = papeleta.generar_codigo

    if request.method == 'POST':
        form = PapeletaForm(request.POST, instance=papeleta)
        if form.is_valid():
            form.save()
            return redirect('papeletas')
    else:
        form = PapeletaForm(instance=papeleta)

    return render(request, 'formulario_papeletas.html', {
        'form': form,
        'papeleta': papeleta  # por si aún lo usas para mostrar en template
    })


def crear_titular(request):
    if request.method == 'POST':
        formulario = TitularForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('titulares')
        else:
            return render(request, 'formulario_titular.html', {'formulario': formulario})

    else:
        formulario_nuevo = TitularForm()
        return render(request, 'formulario_titular.html', {'formulario': formulario_nuevo})


def registrar_usuario(request):
    form = RegistroFormulario()
    if request.method == 'POST':
        form = RegistroFormulario(request.POST)

        if form.is_valid():
            usuario_nuevo = form.save(commit=False)
            usuario_nuevo.set_password(form.cleaned_data['password'])
            usuario_nuevo.save()
            return redirect('login')
    else:
        return render(request, "registro.html", {'form': form})


def loguearse(request):
    form = LoginFormulario()
    if request.method == 'POST':
        form = LoginFormulario(request, data=request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            usuario = authenticate(request, email=email, password=password)
            if usuario is not None:
                login(request, usuario)
                return redirect('home')
    else:
        return render(request, "login.html", {'form': form})


def logout_usuario(request):
    logout(request)
    return redirect('login')


def error_403(request, exception=None):
    return render(request, '403.html', status=403)


def error_404(request, exception=None):
    return render(request, '404.html', status=404)


def ir_tienda(request):
    listado_productos = Producto.objects.all()
    return render(request, 'tienda.html', {'productos': listado_productos})


def add_carrito(request, id):
    carrito = request.session.get('carrito', {})
    producto_en_carrito = carrito.get(str(id), 0)

    # Comprobar si en session existe el id del producto
    if producto_en_carrito == 0:
        # NO
        # lo añado nuevo y en la cantidad -> 1
        carrito[str(id)] = 1

    else:
        # SI
        # cantidad + 1
        carrito[str(id)] += 1

    request.session['carrito'] = carrito
    messages.success(request, "Producto añadido correctamente al carrito.")

    return redirect('tienda')


def ver_carrito(request):
    carrito = {}
    total = 0.0
    carrito_session = request.session.get('carrito', {})

    # Recuperar de session todos mis productos y sus cantidades
    for k, v in carrito_session.items():
        producto = Producto.objects.get(id=k)
        carrito[producto] = v
        total += producto.precio * v

    return render(request, 'carrito.html', {'carrito': carrito, 'total': total})


def restar_carrito(request, id):
    carrito = request.session.get('carrito', {})
    producto_id = str(id)

    if producto_id in carrito:
        if carrito[producto_id] > 1:
            carrito[producto_id] -= 1
        else:
            del carrito[producto_id]  # si llega a 0, lo quitamos

    request.session['carrito'] = carrito
    return redirect('ver_carrito')


def sumar_carrito(request, id):
    carrito = request.session.get('carrito', {})
    producto_id = str(id)

    carrito[producto_id] = carrito.get(producto_id, 0) + 1

    request.session['carrito'] = carrito
    return redirect('ver_carrito')  # importante: vuelve al carrito


def quitar_de_carrito(request, id):
    carrito = request.session.get('carrito', {})
    producto_id = str(id)

    del carrito[producto_id]

    request.session['carrito'] = carrito
    return redirect('ver_carrito')


def comprar(request):
    nuevo_pedido = Pedido()
    nuevo_pedido.codigo = 'CP0001'
    nuevo_pedido.fecha = datetime.now()
    nuevo_pedido.hermano = request.user

    carrito_session = request.session.get('carrito', {})

    for k, v in carrito_session.items():
        linea_pedido = LineaPedido()
        producto = Producto.objects.get(id=k)
        linea_pedido.producto = producto
        linea_pedido.precio = producto.precio
        linea_pedido.cantidad = v
        linea_pedido.pedido = nuevo_pedido
        linea_pedido.save()

    nuevo_pedido.save()
