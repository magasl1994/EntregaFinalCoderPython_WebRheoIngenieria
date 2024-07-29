from django.db import models

class nosotros(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return self.titulo

class servicios(models.Model):
    nombre_servicio = models.CharField(max_length=100)
   
    def __str__(self):
        return self.nombre

class contacto(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    mensaje = models.TextField()

    def __str__(self):
        return f'{self.nombre} - {self.email}'

class Experiencia(models.Model):
    nombre_experiencia = models.CharField(max_length=100)
    descripcion_experiencia = models.TextField()

    def __str__(self):
        return self.nombre_experiencia
