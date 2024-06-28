from django.shortcuts import render

# Create your views here.
def index(request):
    context={}
    return render(request, 'tienda/index.html',context)

def alfajores(request):
    context={}
    return render(request,'tienda/alfajores.html',context)

def oEspeciales(request):
    context={}
    return render(request,'tienda/oEspeciales.html',context)

def ofertas(request):
    context={}
    return render(request,'tienda/ofertas.html',context)

def conocenos(request):

    historia_p1 = "Desde muy joven, Amanda, dueña de “Pipo alfajorería”, mostró un gran amor por los dulces que preparaba su abuela, en especial por los alfajores, una delicia tradicional que aprendió a hacer gracias a ella. A los 18 años y debido a dificultades económicas, Amanda decidió comenzar a vender alfajores por las calles de su ciudad."
    historia_p2 = "Con un carrito lleno de alfajores caseros y una sonrisa, Amanda recorría plazas, mercados y eventos locales. Su dedicación y la calidad de sus productos hicieron que rápidamente se ganara una clientela fiel. A pesar de las dificultades y los desafíos de la vida de un vendedor ambulante, Amanda nunca perdió la pasión por lo que hacía."
    historia_p3 = "A medida que sus alfajores ganaban popularidad, Amanda comenzó a soñar con abrir su propia tienda. Apasionada de la estética victoriana, soñaba con un lugar que combinara su amor por los alfajores y esa elegante época. Durante siete años, ahorró cada peso que pudo, se educó en administración y perfeccionó sus recetas."
    historia_p4 = "Finalmente, a los 25 años, Amanda logró abrir su alfajorería-cafetería, ""Pipo alfajorería"", en el corazón de su ciudad y ha logrado ser un lugar muy querido por sus visitantes. Amanda continúa dedicándose a sus alfajores siempre buscando nuevas formas de sorprender y deleitar a sus clientes con su creatividad culinaria."
    context={"historia_p1":historia_p1,"historia_p2":historia_p2,"historia_p3":historia_p3,"historia_p4":historia_p4}
    return render(request, 'tienda/conocenos.html',context)

def visitanos(request):
    context={}
    return render(request, 'tienda/visitanos.html',context)

