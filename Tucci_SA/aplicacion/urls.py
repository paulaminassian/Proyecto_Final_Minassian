from django.urls import path, include
from .views import *

urlpatterns = [
    
    path('', home, name = "home"),
    path('clientes/', clientes, name = "clientes"),
    path('maritimas/', maritimas, name = "maritimas"),
    path('rutas/', rutas, name = "rutas"),
    path('precios/', precios, name = "precios"),
]
