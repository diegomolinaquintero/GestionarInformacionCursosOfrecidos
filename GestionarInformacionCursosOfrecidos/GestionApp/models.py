from django.db import models
from django.core.exceptions import ValidationError
import re



def caracteres_especiales_validator(value):
    if any(char in value for char in '!@#$%^&*(),.?":{}|<>'):
        raise ValidationError("No debe contener caracteres especiales.")

def sin_arrobas_validator(value):
    if '@' in value:
        raise ValidationError("No debe contener arrobas.")

def sin_numeros_validator(value):
    if any(char.isdigit() for char in value):
        raise ValidationError("Nombre No debe contener números.")

def sin_palabras_prohibidas_validator(value):
    if re.search(r'\bfont\b|\bint\b', value, re.I):
        raise ValidationError("ningun texto No debe contener las palabras 'font' o 'int'.")

def sin_etiquetas_html_validator(value):
    if re.search(r'<\s*[^>]*>', value):
        raise ValidationError("ningun texto debe No debe contener etiquetas HTML.")

def precio_no_blanco_validator(value):
    if not value:
        raise ValidationError("El precio no debe estar en blanco.")

def precio_positivo_validator(value):
    if value <= 0:
        raise ValidationError("El precio debe ser un número positivo.")

class Docente(models.Model):
    nombre = models.CharField(blank=False,max_length=50, validators=[
        
        caracteres_especiales_validator,
        sin_arrobas_validator,
        sin_numeros_validator,
        sin_palabras_prohibidas_validator,
        sin_etiquetas_html_validator
    ])
    documento = models.CharField(unique=True, blank=False,max_length=20, validators=[
        
        caracteres_especiales_validator,
        sin_arrobas_validator,
        sin_palabras_prohibidas_validator,
        sin_etiquetas_html_validator
    ])
    correo = models.EmailField(unique=True, )

    def __str__(self):
        return self.nombre

class Curso(models.Model):
    nombre = models.CharField(blank=False,max_length=50, validators=[
        
        caracteres_especiales_validator,
        sin_arrobas_validator,
        sin_numeros_validator,
        sin_palabras_prohibidas_validator,
        sin_etiquetas_html_validator
    ])
    descripcion = models.TextField(blank=False,max_length=50,validators=[
        
        sin_palabras_prohibidas_validator,
        sin_etiquetas_html_validator
    ])
    duracion_semanas = models.PositiveIntegerField()
    precio = models.DecimalField(blank=False,max_digits=10, decimal_places=2, validators=[
        precio_no_blanco_validator,
        precio_positivo_validator   
    ])
    fecha_inicio = models.DateTimeField()
    docente = models.ForeignKey(Docente, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.nombre