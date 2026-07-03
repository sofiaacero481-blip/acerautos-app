from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from apl.models import *
# Create your views here.

#def vista1(request):
   

  #  return render(request,'index2.html')

def vista2():
    persona ={
        
        'Nombre': 'Fabian',
        'Apellido': 'Alvarez',
        'Categorias': Categoria.objects.all() 
    }
    return  (persona)

def vista3(request):
    persona = vista2()

    return render(request, 'index.html',{'persona': persona})