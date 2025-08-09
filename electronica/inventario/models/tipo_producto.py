from django.db import models
class tipoProducto(models.Model):
    id = models.PositiveSmallIntegerField(default=3, primary_key=True)
    nombre = models.CharField(max_length=20)

def __str__(self):
    return self.nombre