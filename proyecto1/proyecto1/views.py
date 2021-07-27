from django.http import HttpResponse
import datetime
from django.template import Template, context

#Primera Vista
def saludo(request):

#Se ocupa html para la primera vista mediante plantillas

    doc_externo = open("C:/Users/robinson.carvallo/Desktop/ProyectoDjango/proyecto1/proyecto1/plantillas/miplantilla.html")
    
    plt = Template(doc_externo.read())

    doc_externo.close()

    ctx = context()

    documento = plt.render(ctx)

    return HttpResponse(documento)

#Segunda Vista
def despedida(request):

    return HttpResponse("Fin de la Pagina")

#Tercera Vista
def dameFecha(request):
    
    #Devuelve Fecha y Hora Actual
    fecha_actual = datetime.datetime.now()

    documento = """<html>
    <body>
    <h2>
    Fecha y hora actuales %s
    </h2>
    </body>
    </html>""" %fecha_actual

    return HttpResponse(documento)

#Cuarta Vista
def calculaEdad(request, edad, agno):

    #edadActual = 32
    periodo = agno - 2021
    edadFutura = edad + periodo
    documento = "<html><body><h2>En el año %s tendras %s años" %(agno, edadFutura)

    return HttpResponse(documento)
