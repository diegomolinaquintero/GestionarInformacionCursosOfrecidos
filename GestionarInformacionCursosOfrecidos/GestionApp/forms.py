from django import forms

from .models import Docente, Curso

class DocenteForm(forms.ModelForm):

    class Meta:
        model = Docente
        fields = ('nombre', 'documento','correo')
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'documento': forms.TextInput(attrs={'class': 'form-control'}),
            'correo': forms.EmailInput(attrs={'class': 'form-control'}),
        }
        
class CursoForm(forms.ModelForm):

    class Meta:
        model = Curso
        fields = ('nombre', 'descripcion','duracion_semanas', 'precio','fecha_inicio', 'docente')
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control'}),
            'duracion_semanas': forms.NumberInput(attrs={'class': 'form-control'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control'}),
            'fecha_inicio': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'docente': forms.Select(attrs={'class': 'form-control'}),
        }