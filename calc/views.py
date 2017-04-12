from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def suma(request, num1, num2):
    resultado = int(num1) + int(num2)
    return HttpResponse("<b><h1>" + str(num1) + " + " +
                        str(num2) + " = " + str(resultado)+ "</h1></b>")

def resta(request, num1, num2):
    resultado = int(num1) - int(num2)
    return HttpResponse("<b><h1>" + str(num1) + " - " +
                        str(num2) + " = " + str(resultado)+ "</h1></b>")

def multi(request, num1, num2):
    resultado = int(num1) * int(num2)
    return HttpResponse("<b><h1>" + str(num1) + " * " +
                        str(num2) + " = " + str(resultado)+ "</h1></b>")

def divi(request, num1, num2):
    try:
        resultado = int(num1) / int(num2)
    except ZeroDivisionError:
          return HttpResponse("<b> ¡Division entre cero! </b>")

    return HttpResponse("<b><h1>" + str(num1) + " / " +
                        str(num2) + " = " + str(resultado)+ "</h1></b>")

def fallo(request):
	return HttpResponse("<b><h1>404 Not Found</h1>" +
                       "Fallo al introducir los numeros</b>")
