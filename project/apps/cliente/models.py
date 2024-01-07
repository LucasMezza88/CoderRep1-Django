from django.db import models

class Pais(models.Model):
    nombre = models.CharField(max_length=100)
	
    def __str__(self):
        return self.nombre
    
    class Meta:
         verbose_name = "país"
         verbose_name_plural = "países"
	
class Cliente(models.Model):
	nombre = models.CharField(max_length=100)
	apellido = models.CharField(max_length=100)
	nacimiento = models.DateField(null=True, blank=True)
	pais_origen_id = models.ForeignKey(Pais, null=True, blank=True, on_delete=models.SET_NULL)
     
	def __str__(self):
            return f"{self.apellido}, {self.nombre}" 