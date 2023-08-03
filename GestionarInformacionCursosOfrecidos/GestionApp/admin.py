from django.contrib import admin
from .models import Docente
from .models import Curso

admin.site.register(Docente)
admin.site.register(Curso)
