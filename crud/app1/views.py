from django.shortcuts import render, get_object_or_404, redirect
from .models import Estudiante
from .forms import EstudianteForm

#CRUD Estudiante
# CREATE Estudiante
# READ Estudiante
# UPDATE Estudiante
# DELETE Estudiante

# read Estudiante (leer todos los registros)
def estudiante_list(request):
    estudiantes = Estudiante.objects.all()
    return render(request, 'app1/estudiante_list.html', {'estudiantes': estudiantes})

#read estudiante (leer un registro)
def estudiante_detail(request, pk):
    estudiante = get_object_or_404(Estudiante, pk=pk)
    return render(request, 'app1/estudiante_detail.html', {'estudiante': estudiante})

# crear estudiante 
def estudiante_create(request):
    if request.method == "POST":
        form = EstudianteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('estudiante_list')
    else:
        form = EstudianteForm()
    return render(request, 'app1/estudiante_form.html', {'form': form})

def estudiante_update(request, pk):
    estudiante = get_object_or_404(Estudiante, pk=pk)
    if request.method == "POST":
        form = EstudianteForm(request.POST, instance=estudiante)
        if form.is_valid():
            form.save()
            return redirect('estudiante_list')
    else:
        form = EstudianteForm(instance=estudiante)
    return render(request, 'app1/estudiante_form.html', {'form': form})

def estudiante_delete(request, pk):
    estudiante = get_object_or_404(Estudiante, pk=pk)
    if request.method == "POST":
        estudiante.delete()
        return redirect('estudiante_list')
    return render(request, 'app1/estudiante_confirm_delete.html', {'estudiante': estudiante})