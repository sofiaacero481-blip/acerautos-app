from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from apl.forms import CategoriaForm
from apl.models import *
from django.views.generic import ListView,CreateView,FormView
from apl.views.categoria.views import *


def Categoria_listar(request):
    data = {
        'categoria':'categoria',
        'titulo': 'Lista de Categorias',
        'categorias': Categoria.objects.all()
    }
    return render(request, 'categoria/lista_categoria.html',data)
#---------------------VIEW LISTAR CATEGORIA---------------------
class CategoriaListView(ListView):
    model = Categoria
    template_name = 'categoria/lista_categoria.html'
    context_object_name = 'categorias'

    
    #@method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
  
  
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Lista de Categorias'
        context['categoria'] = 'categoria' 

        return context
    
    #------------------VIEW CREAR CATEGORIA -----------------------------
    

    