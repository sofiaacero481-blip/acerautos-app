from django.urls import path
from apl.views import *
from apl.views.categoria.views import *# categoria


app_name = 'apl'

urlpatterns = [
    path('categoria/listar/',CategoriaListView.as_view(), name='categoria_lista'),# ruta
    #path('categoria/crear/',CategoriaCreateView.as_view(), name='categoria_crear'),# 
]
