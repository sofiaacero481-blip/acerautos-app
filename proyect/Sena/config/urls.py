"""
URL configuration for apps project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from apl.views import *
#from login.views import Login_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path ('login/',include('login.urls')),
    # path('prueba/',vista1), # ruta de la vista1
    # path('dic/',vista2), # prueba con diccionario
    # path('pagina/',vista3) # pagina html
    path('apl/', include('apl.urls')),
]
