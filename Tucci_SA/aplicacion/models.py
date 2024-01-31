from django.db import models

# Create your models here.

class Clientes(models.Model):
    razon_social = models.CharField(max_length=50)
    contacto = models.EmailField()

class Maritimas(models.Model):
    razon_social = models.CharField(max_length=50)
    contacto = models.EmailField()
    
class Rutas(models.Model):
    codigo = models.IntegerField()
    origen = models.CharField(max_length=50)
    destino = models.CharField(max_length=50) 
    
class Precios(models.Model):
    ruta = models.IntegerField()
    precio=models.IntegerField()

