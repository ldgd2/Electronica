from django.db import models
from productos import producto
class accesorios(models.Model):
    codigoAccesorio = models.ForeignKey(
        producto,
        primary_key= True,
        max_length=20,
        on_delete=models.PROTECT,
    )
    codigoProductoBase = models.ForeignKey(
        producto,
        primary_key=True, 
        max_length=20,
         on_delete=models.PROTECT
    )
def __str__(self):
    return