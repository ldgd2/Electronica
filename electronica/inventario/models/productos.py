from django.db import models
from tipo_producto import tipoProducto
from unidad_medida import unidadMedida
from marcas import marca
class producto(models.Model):
    codigo = models.CharField(max_length=20,primary_key=True)
    nombre = models.CharField(max_legth = 100, null= False)
    nombre = models.CharField(max_legth = 100)
    precio = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    descripcion = models.CharField(max_length=500, null=True)
    imagen = models.ImageField(upload_to='productos/', null=True, blank=True)
    

    idTipo = models.ForeignKey(
        tipoProducto,
        on_delete=models.PROTECT,
        default=3
    )
    idUnidad = models.ForeignKey(
        marca,
        on_delete=models.PROTECT,
        default= 4

    )

    codigoMarca = models.ForeignKey(
        marca,
        on_delete=models.PROTECT

    )



    def __str__ (self):
        return self.nombre