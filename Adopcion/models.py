from django.db import models

class Adopcion(models.Model):
    nombre = models.CharField(max_length=100)
    fecha = models.DateField()
    observaciones = models.TextField(blank=True, null=True)