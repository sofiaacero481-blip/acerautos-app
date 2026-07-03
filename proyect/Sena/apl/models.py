from django.db import models
from datetime import datetime
from decimal import Decimal
from apl.choices import opc_generos

# Create your models here.
#------------Entidad categorias----------------------------

class Categoria(models.Model):
    nombre = models.CharField(max_length=100,verbose_name='Nombre',unique=True)
    def __str__(self):
        return self.nombre
    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        
#-------------Entidad producto ---------------------------
class Producto(models.Model):
    nombre = models.CharField(max_length=100,verbose_name='Nombre',unique=True)
    categ = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='product/%y/%m/%d',null=True,blank=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
class Cliente(models.Model):
        nombres = models.CharField(max_length=150, verbose_name='Nombres')
        Apellidos = models.CharField(max_length=150, verbose_name='Apellidos')
        Cedula = models.CharField(max_length=10, unique=True, verbose_name='Cedula')
        Fecha_n = models.DateField(default=datetime.now, verbose_name='Fecha de nacimiento')
        Direccion = models.CharField(max_length=150, null=True, blank=True, verbose_name='Dirección')
        sexo = models.CharField(max_length=10, choices=opc_generos, default='masculino', verbose_name='Sexo')

        def __str__(self):
            return self.nombres

        class Meta: #clase meta permite renombrar tabla y atributos que se crea por defecto
            verbose_name = 'Cliente'
            verbose_name_plural = 'Clientes'
            db_table ='Cliente'
            #ordering = [id]  

# #------------------Entidad Venta----------------------------------------------------------------
class Venta(models.Model):
        id = models.AutoField(primary_key=True)
        cli = models.ForeignKey(Cliente, on_delete=models.CASCADE)
        fecha_ingreso = models.DateField(default=datetime.now)
        subtotal = models.DecimalField(default=Decimal('0.00'), max_digits=9, decimal_places=2)
        iva = models.DecimalField(default=Decimal('0.00'), max_digits=9, decimal_places=2)
        total = models.DecimalField(default=Decimal('0.00'), max_digits=9, decimal_places=2)

        def __str__(self):
            return self.id

        class Meta: #clase meta permite renombrar tabla y atributos que se crea por defecto
            verbose_name = 'Venta'
            verbose_name_plural = 'Ventas'
            db_table ='Venta'
            # ordering = [id] 
# #---------------- Entidad Detalle_Venta------------------------------------------------------------------

class Det_venta(models.Model):
    id = models.AutoField(primary_key=True)
    fk_venta = models.ForeignKey(Venta, on_delete=models.CASCADE, related_name='detalles')
    prod = models.ForeignKey(Producto, on_delete=models.CASCADE)
    precio = models.DecimalField(default=Decimal('0.00'), max_digits=9, decimal_places=2)
    cant = models.IntegerField(default=0)
    subtotal = models.DecimalField(default=Decimal('0.00'), max_digits=9, decimal_places=2)
    
    def __str__(self):
        return self.id

    class Meta:
        verbose_name = 'Detalle de Venta'
        verbose_name_plural = 'Detalle de Ventas'
        db_table ='D_Venta'
        # ordering = ['id']        
