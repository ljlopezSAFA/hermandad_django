from django.shortcuts import render, redirect, get_object_or_404
from hermandapp.forms import *
from hermandapp.models import *


def go_home(request):
    return render(request, 'home.html')


def go_about_us(request):
    return render(request, 'about_us.html')


def go_templo_page(request):
    return render(request, 'templo.html')


def cargar_listado_hermanos(request):
    lista_hermanos = Hermano.objects.all()
    return render(request, 'hermanos.html', {'hermanos': lista_hermanos})


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


def eliminar_hermano(request, id):
    hermano = get_object_or_404(Hermano, id=id)  # Si existe, lo obtenemos

    if hermano:
        hermano.delete()

    return redirect('hermanos')



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





def crear_titular_default(request):
    titular = Titular.objects.create(
        nombre="Nuestro Padre Jesús del Silencio",
        descripcion="El Señor del Silencio en el Desprecio de Herodes es una obra realizada por el taller de Pedro Roldán en 1698. No está documentada la autoría, pero sí posee la Hermandad el encargo que realizara a dicho taller para la ejecución de la talla.",
        autor="Pedro Roldán",
        anyo=1698,
        imagen="https://i0.wp.com/lascofradiasdesevilla.com/wp-content/uploads/2014/05/JAC_0280.jpg?resize=600%2C530&ssl=1",
        procesiona=True)

    titular2 = Titular.objects.create(
        nombre="María Santísima de la Amargura",
        descripcion="La Imagen de María Santísima de la Amargura es obra anónima fechada a principios del siglo XVIII, pues en los inventarios de la Hermandad de 1.708 en adelante, aparece ya una Imagen “con cabeza, manos y pie de candelero”. Fue en 1.763 cuando Benito de Hita y Castillo le hace nuevo cuerpo y candelero para adaptarle la posición dialogante con San Juan.",
        autor="Anónimo",
        anyo=1708,
        imagen="https://www.sevillaactualidad.com/wp-content/uploads/2020/02/amargura.jpg",
        procesiona=True)

    print("Titular creado->", titular)
    return redirect('titulares')


