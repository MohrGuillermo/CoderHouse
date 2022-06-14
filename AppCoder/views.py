
from django.http import HttpResponse
from django.shortcuts import render
from AppCoder.models import Curso, Estudiante, Profesor, Entregable
from AppCoder.forms import CursoFormulario, ProfesorFormulario, EstudianteFormulario, EntregableFormulario
 
#  ACA ES DONDE VAMOS A CREAR REALMENTE LOS FORMULARIOS MEDIANTE EL API DE DJANGO, ES DECIR, UNA HERRAMIENTA QUE PERMITE HACER MUCHO MAS FACIL Y DINAMICA LA CREACION DE FORMULARIOS, YA QUE UNA VEZ DETERMINADA LA CLASE EN FORMS.PY NO HARA FALTA NOMBRAR CADA UNA DE LAS VARIABLES A AGREGAR DESPUES. (SIGUE EN URLS.PY)

def inicio(request):
    return render(request, 'Inicio.html')


def curso(request):
    lista_cursos = Curso.objects.all()
    return render(request, 'AppCoder/template_cursos.html', {'lista_cursos':lista_cursos})


def cursoFormulario(request):
    
    if request.method == 'POST':
        miFormulario = CursoFormulario(request.POST)

        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            nombre = informacion['curso']
            comision = informacion['comision']
            curso = Curso(nombre=nombre, comision=comision)
            curso.save()
            return render(request, 'AppCoder/Inicio.html')
    
    else:
        miFormulario= CursoFormulario()


# BUSQUEDA DE DATOS

def busquedaDeComision(request):

    return render(request, 'buscadorComision.html')


def buscar(request):
    
    respuesta = f"Estoy buscando la comision Nº: { request.GET['comision'] }"
    if request.GET['comision']:
        comision = request.GET['comision']
        cursos = Curso.objects.filter(comision=comision)
        return render(request, 'AppCoder/resultadosBusqueda.html', {'cursos':cursos, 'comision':comision},)
    else:
        respuesta = 'No se ingresó ningúna comisión'
        return render(request, 'AppCoder/resultadosBusqueda.html', {'respuesta':respuesta})
    





def estudiante(request):
    return render(request, 'template_estudiantes.html')  
# FORMULARIO COMUN
# def formularioEstudiante(request):
#     if request.method == 'POST':
#         estudiante = Estudiante(request.POST['nombre'], request.POST['apellido'], request.POST['email'])
#         estudiante.save()
#         return render(request, 'AppCoder/Inicio.html')
#     return render(request, 'formulario_estudiante.html')

def formularioEstudiante(request):
    if request.method == 'POST':
        miFormulario = EstudianteFormulario(request.POST)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            nombre = informacion['nombre']
            apellido = informacion['apellido']
            email = informacion['email']
            estudiante = Estudiante(nombre=nombre, apellido=apellido, email=email)
            estudiante.save()
            return render(request, 'AppCoder/Inicio.html')
    else:
        miFormulario = EstudianteFormulario()    
    
    return render(request, 'FormularioEstudiante.html', {'miFormulario':miFormulario})



def entregable(request):
    return render(request, 'template_entregables.html'  )

def formularioEntregable(request):
    if request.method == 'POST':
        miFormulario = EntregableFormulario(request.POST)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            nombre = informacion['nombre']
            fecha_de_entrega = informacion['fecha_de_entrega']
            entregado = informacion['entregado']
            entregable = Entregable(nombre=nombre, fecha_de_entrega=fecha_de_entrega, entregado=entregado)
            entregable.save()
            return render(request, 'AppCoder/Inicio.html')
    else:
        miFormulario = EntregableFormulario()    
    return render(request, 'FormularioEntregable.html', {'miFormulario':miFormulario})


   

def verProfesores(request):
    profesores = Profesor.objects.all()
    return render(request, 'AppCoder/template_profesores.html', {'profesores':profesores})


def formularioProfesor(request):
    if request.method == 'POST':
        miFormulario = ProfesorFormulario(request.POST)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            nombre = informacion['nombre']
            apellido = informacion['apellido']
            email = informacion['email']
            profesion = informacion['profesion']
            profesor = Profesor(nombre=nombre, apellido=apellido, email=email, profesion=profesion)
            profesor.save()
            return render(request, 'AppCoder/inicio.html')
    else:
        miFormulario = ProfesorFormulario()    
    return render(request, 'FormularioProfesores.html', {'miFormulario':miFormulario})

# CRUD de eliminacion.
def eliminarProfesor(request, nombre):
    profesor = Profesor.objects.get(nombre=nombre)
    profesor.delete()
    profesores = Profesor.objects.all()
    contexto = {'profesores':profesores}
    return render(request, 'AppCoder/template_profesores.html', contexto)
    