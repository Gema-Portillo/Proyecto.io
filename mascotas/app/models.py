from django.db import models

# Create your models here.
from django.db import models

class Mascota(models.Model):
    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=50) 
    edad = models.IntegerField()
    dueño_email = models.EmailField()

    def __str__(self):
        return self.nombre
