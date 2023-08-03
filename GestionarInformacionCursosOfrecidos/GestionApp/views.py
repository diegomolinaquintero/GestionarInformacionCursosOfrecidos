from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect
from .forms import DocenteForm, CursoForm
from .models import Docente, Curso

def home_view(request):
    # Puedes agregar lógica adicional aquí si es necesario
    return render(request, 'GestionApp/home.html') 


# Vistas para Docentes

@csrf_exempt
def docente_list(request):
    if request.method == 'GET':
        docentes = Docente.objects.all().order_by('nombre')
        return render(request, 'GestionApp/VerDocente.html', {'docentes': docentes})

@csrf_exempt   
def docente_new(request):
    if request.method == "POST":
        form = DocenteForm(request.POST)
        if form.is_valid():
            docente = form.save(commit=False)
            docente.save()
            return redirect('docente_detail', pk=docente.pk)
    else:
        form = DocenteForm()
    return render(request, 'GestionApp/DocenteNuevo.html', {'form': form})
    
    
    
@csrf_exempt
def docente_detail(request, pk):
    docente = get_object_or_404(Docente, pk=pk)
    
    if request.method == 'GET':
        return render(request, 'GestionApp/DocenteDetalle.html', {'docente': docente})


@csrf_exempt
def docente_delete(request, pk):
    if request.method == "POST":
        docente = get_object_or_404(Docente, pk=pk)
        docente.delete()
        docentes = Docente.objects.all().order_by('nombre')
        return render(request, 'GestionApp/VerDocente.html', {'docentes': docentes})

@csrf_exempt
def docente_edit(request, pk):
    print(request)
    docente = get_object_or_404(Docente, pk=pk)
    if request.method == "POST":
        form = DocenteForm(request.POST, instance=docente)
        if form.is_valid():
            docente = form.save()  # Guarda los cambios en el modelo automáticamente
            return redirect('docente_detail', pk=docente.pk)
    else:
        form = DocenteForm(instance=docente)
    return render(request, 'GestionApp/DocenteEdit.html', {'form': form})


# Vistas para Cursos

@csrf_exempt
def curso_list(request):
    if request.method == 'GET':
        cursos = Curso.objects.all().order_by('nombre')
        return render(request, 'GestionApp/VerCursos.html', {'cursos': cursos})

@csrf_exempt   
def curso_new(request):
    if request.method == "POST":
        form = CursoForm(request.POST)
        if form.is_valid():
            curso = form.save(commit=False)
            curso.save()
            return redirect('curso_detail', pk=curso.pk)
    else:
        form = CursoForm()
    return render(request, 'GestionApp/CursoNuevo.html', {'form': form})
    
    
    
@csrf_exempt
def curso_detail(request, pk):
    curso = get_object_or_404(Curso, pk=pk)

    if request.method == 'GET':
        return render(request, 'GestionApp/CursoDetalle.html', {'curso': curso})


@csrf_exempt
def curso_delete(request, pk):
    if request.method == "POST":
        curso = get_object_or_404(Curso, pk=pk)
        curso.delete()
        cursos = Curso.objects.all().order_by('nombre')
        return render(request, 'GestionApp/VerCursos.html', {'cursos': cursos})

@csrf_exempt
def curso_edit(request, pk):
    print(request)
    curso = get_object_or_404(Curso, pk=pk)
    if request.method == "POST":
        form = CursoForm(request.POST, instance=curso)
        if form.is_valid():
            curso = form.save()  # Guarda los cambios en el modelo automáticamente
            return redirect('curso_detail', pk=curso.pk)
    else:
        form = CursoForm(instance=curso)
    return render(request, 'GestionApp/CursoEdit.html', {'form': form})
