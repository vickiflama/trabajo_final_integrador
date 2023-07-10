from django.db import models

# Create your models here.

class Perfil(models.Model):
    class Meta:
        db_table = "app_perfiles_perfil"

    nombre  =  models.CharField(max_length=200)
    telefono = models.IntegerField()
    email  = models.EmailField(max_length=40)
    domicilio   = models.CharField(max_length=200)

    def __str__(self):
        return f"Perfil: {self.nombre} vive en {self.domicilio}"

    def obtener_campos_valores(self):
        return [
            (field.verbose_name, field.value_from_object(self))
            for field in self.__class__._meta.fields[1:]
        ]