from django.db import models

# Create your models here.
class Persona(models.Model):
    
    nombres = models.CharField(max_length=30)
    apellidos = models.CharField(max_length=30)
    cedula = models.CharField(max_length=30, unique=True)
    correo = models.CharField(max_length=30)

    def __str__(self):
        return "%s %s %s %s" % (self.nombres,
                self.apellidos,
                self.cedula,
                self.correo)

class Barrio(models.Model):
    nombreBa = models.CharField(max_length=100)
    siglas = models.CharField(max_length=100)
    def __str__(self):
        return "%s %s " % (self.nombreBa,
                self.siglas)
 
          
class LocalComida (models.Model):
    direccion = models.CharField(max_length=100)
    tipoComida = models.CharField(max_length=100)
    ventasPMes =models.IntegerField()
    propietario = models.ForeignKey(Persona, on_delete=models.CASCADE,
            related_name="propC")
    barrio = models.ForeignKey(Barrio, on_delete=models.CASCADE,
            related_name="barrioC")
    def get_valor(self):
        """
        """
        valor = self.ventasPMes
        valorPer = valor * 0.8
        return valorPer
    
    def __str__(self):
        return "%s %s %d %s %s" % (self.direccion,
                self.tipoComida,
                self.ventasPMes,
                self.propietario,
                self.barrio)
    
class LocalRepuestos (models.Model):
    direccion = models.CharField(max_length=100)
    valorTMercaderia = models.IntegerField()
    propietario = models.ForeignKey(Persona, on_delete=models.CASCADE,
            related_name="propR")
    barrio = models.ForeignKey(Barrio, on_delete=models.CASCADE,
            related_name="barrioR")
    def get_valor(self):
        """
        """
        valor = self.valorTMercaderia
        valorPer = valor * 0.001
        return valorPer
        
    def __str__(self):
        return "%s %d %s %s " % (self.direccion,
                self.valorTMercaderia,
                self.propietario,
                self.barrio)
        