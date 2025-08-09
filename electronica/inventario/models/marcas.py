from django.db import models
class marca(models.Model):
    codigo = models.CharField(max_lenght = 20, unique = True, primary_key = True)
    nombre = models.CharField(max_legth = 100)

    def __str__ (self):
        return self.nombre