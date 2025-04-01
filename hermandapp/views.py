from django.shortcuts import render, redirect
from hermandapp.models import *


def go_home(request):
    return render(request, 'home.html')


def go_about_us(request):
    return render(request, 'about_us.html')


def go_templo_page(request):
    return render(request, 'templo.html')

def cargar_listado_hermanos(request):
    lista_hermanos = Hermano.objects.all()
    return render(request, 'hermanos.html', { 'hermanos': lista_hermanos})
























def go_titulares(request):
    list_titulares = Titular.objects.all()
    return render(request, 'titulares.html', {'titulares': list_titulares})


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
