from django.shortcuts import render, redirect
from .forms import ProfesorForm, CursoForm, EstudianteForm, EntregableForm
from .models import Curso

def agregar_profesor(request):
    if request.method == 'POST':
        form = ProfesorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('agregar_profesor')
    else:
        form = ProfesorForm()
    return render(request, 'miapp/profesor_form.html', {'form': form})

def agregar_curso(request):
    if request.method == 'POST':
        form = CursoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('agregar_curso') 
    else:
        form = CursoForm()
    return render(request, 'miapp/curso_form.html', {'form': form})

def agregar_estudiante(request):
    if request.method == 'POST':
        form = EstudianteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('agregar_estudiante') 
    else:
        form = EstudianteForm()
    return render(request, 'miapp/estudiante_form.html', {'form': form})

def agregar_entregable(request):
    if request.method == 'POST':
        form = EntregableForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('agregar_entregable') 
    else:
        form = EntregableForm()
    return render(request, 'miapp/entregable_form.html', {'form': form})

def buscar_curso(request):
    cursos = []
    if 'camada' in request.GET:
        camada = request.GET['camada']
        cursos = Curso.objects.filter(camada=camada)
    return render(request, 'miapp/buscar_curso.html', {'cursos': cursos})

def acerca_de_mi(request):
    return render(request, 'miapp/acerca_de_mi.html')
