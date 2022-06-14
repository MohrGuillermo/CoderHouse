

from django.db import models
# LOS MODELOS SON LO PRIMERO QUE SE CREA YA QUE SON LOS CLASES QUE DETERMINARAN LOS OBJETOS QUE PODREMOS CARGAR EN NUESTRA WEB (SIGUE EN FORMS.PY)


class Curso(models.Model):
    nombre = models.CharField(max_length=40)
    comision = models.IntegerField()
    def __str__(self) -> str:
        return f'Nombre: {self.nombre}, Comision: {self.comision}'


class Estudiante(models.Model):
    nombre = models.CharField(max_length=40)
    apellido =models.CharField(max_length=40)
    email = models.EmailField()
    def __str__(self) -> str:
        return f'Nombre: {self.nombre}, Apellido: {self.apellido}, E-mail: {self.email}'


class Profesor(models.Model):
    nombre = models.CharField(max_length=40)
    apellido =models.CharField(max_length=40)
    email = models.EmailField()
    profesion = models.CharField(max_length=40)
    def __str__(self) -> str:
        return f'Nombre: {self.nombre}, Apellido: {self.apellido}, E-mail: {self.email}, Profesion: {self.profesion}'



class Entregable(models.Model):
    nombre = models.CharField(max_length=40)
    fecha_de_entrega = models.DateField()
    entregado = models.BooleanField()
    def __str__(self) -> str:
        return f'Nombre: {self.nombre}, Fecha limite: {self.fecha_de_entrega}'

        