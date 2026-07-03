from django.urls import path
from login.views import *

urlpatterns = [
    path ('',Login_view.as_view()),
    path ('login/',Login_view.as_view(),name='login'),
    path ('/logout/',logoutredirect.as_view(),name='logout')
]