from django.db import models
from django.urls import reverse # Used to generate URLs by reversing the URL patterns
import uuid # Required for unique book instances

class Auto(models.Model):
	nombre = models.CharField(max_length=200)

	CANTIDAD = (
		('1', 'Una'),
		('2', 'Dos'),
		('3', 'Tres'),
		('4', 'Cuatro'),
	)

	cabina = models.IntegerField(
		max_length=1,
		choices=CANTIDAD,
		default='1',
		help_text='Cantidad de asientos',
	)

	modelo = models.CharField(max_length=50)
	marca = models.CharField(max_length=50)
	imagen = models.CharField(max_length=200)

	def __str__(self):
		return self.nombre