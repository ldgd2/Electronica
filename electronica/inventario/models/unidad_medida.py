from django.db import models
class unidadMedida(models.Model):
    id = models.PositiveSmallIntegerField(default=4, unique = True, primary_key = True)
    nombre = models.CharField(max_legth = 50, null= False)

    def __str__ (self):
        return self.nombre