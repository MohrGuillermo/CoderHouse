
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

def busquedaDeComision(request):
    return render(request, 'buscadorComision.html')

def buscar(request):
    if request.GET['comision']:
        comision = request.GET['comision']
        cursos = Curso.objects.filter(comision=comision)
        return render(request, 'AppCoder/resultadosBusqueda.html', {'cursos':cursos, 'comision':comision},)
    else:
        respuesta = 'No se ingresó ningúna comisión'
        return render(request, 'AppCoder/resultadosBusqueda.html', {'respuesta':respuesta})

def eliminarCurso(request, nombre):
    curso = Curso.objects.get(nombre=nombre)
    curso.delete()
    cursos = Curso.objects.all()
    contexto = {'cursos':cursos}
    return render(request, 'AppCoder/template_cursos.html', contexto)
    
def editarCurso(request, nombre):
    curso = Curso.objects.get(nombre=nombre)

    if request.method == 'POST':
        miFormulario = CursoFormulario(request.POST)

        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            curso.nombre = informacion['nombre']
            curso.comision = informacion['comision']

            curso.save()

            return render(request, 'AppCoder/inicio.html')

    else:
        miFormulario = CursoFormulario(initial={'nombre':curso.nombre, 'comision':curso.comision})
    
    return render(request, 'editarCurso.html', {'miFormulario':miFormulario, 'nombre':nombre})
            


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




def estudiante(request):
    estudiantes = Estudiante.objects.all()
    return render(request, 'template_estudiantes.html' , {'estudiantes':estudiantes})  
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


def buscarEstudiante(request):
    return render(request, 'buscarEstudiante.html')

def encontrarEstudiante(request):
    if request.GET['nombre']:
        nombre = request.GET['nombre']
        estudiantes = Estudiante.objects.filter(nombre=nombre)
        return render(request, 'AppCoder/resultadosEstudiante.html', {'nombre':nombre, 'estudiantes':estudiantes})
    else:
        respuesta = 'No se ingresó ningún estudiante con ese nombre'
        return render(request, 'AppCoder/resultadosEstudiante.html', {'respuesta':respuesta})

def eliminarEstudiante(request, nombre):
    estudiante = Estudiante.objects.get(nombre=nombre)
    estudiante.delete()
    estudiantes = Estudiante.objects.all()
    contexto = {'estudiantes':estudiantes}
    return render(request, 'AppCoder/template_estudiantes.html', contexto)

def editarEstudiante(request, nombre):
    estudiante = Estudiante.objects.get(nombre=nombre)

    if request.method == 'POST':
        miFormulario = EstudianteFormulario(request.POST)

        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            estudiante.nombre = informacion['nombre']
            estudiante.apellido = informacion['apellido']
            estudiante.email = informacion['email']

            estudiante.save()

            return render(request, 'AppCoder/inicio.html')

    else:
        miFormulario = EstudianteFormulario(initial={'nombre':estudiante.nombre, 'apellido':estudiante.apellido, 'email':estudiante.email})
    
    return render(request, 'editarEstudiante.html', {'miFormulario':miFormulario, 'nombre':nombre})


# def eliminarCurso(request, nombre):
#     curso = Curso.objects.get(nombre=nombre)
#     curso.delete()
#     cursos = Curso.objects.all()
#     contexto = {'cursos':cursos}
#     return render(request, 'AppCoder/template_cursos.html', contexto)
    
# def editarCurso(request, nombre):
#     curso = Curso.objects.get(nombre=nombre)

#     if request.method == 'POST':
#         miFormulario = CursoFormulario(request.POST)

#         if miFormulario.is_valid:
#             informacion = miFormulario.cleaned_data
#             curso.nombre = informacion['nombre']
#             curso.comision = informacion['comision']

#             curso.save()

#             return render(request, 'AppCoder/inicio.html')

#     else:
#         miFormulario = CursoFormulario(initial={'nombre':curso.nombre, 'comision':curso.comision})
    
#     return render(request, 'editarCurso.html', {'miFormulario':miFormulario, 'nombre':nombre})
            
    






def entregable(request):
    entregables = Entregable.objects.all()
    return render(request, 'template_entregables.html', {'entregables':entregables})

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

def eliminarEntregable(request, nombre):
    entregable = Entregable.objects.get(nombre=nombre)
    entregable.delete()
    entregables = Entregable.objects.all()
    contexto = {'entregables':entregables}
    return render(request, 'AppCoder/template_entregables.html', contexto)


def editarEntregable (request, entregable_nombre):
    entregable = Entregable.objects.get(nombre=entregable_nombre)
    if request.method == 'POST':
        miFormulario = EntregableFormulario(request.POST)

        if miFormulario.is_valid(): # Si el formulario es valido, se guarda.
            informacion = miFormulario.cleaned_data
            entregable.nombre = informacion['nombre']
            entregable.fecha_de_entrega = informacion['fecha_de_entrega']
            entregable.entregado = informacion['entregado']
            entregable.save()

            return render(request, 'AppCoder/inicio.html') 

    else:
        miFormulario = EntregableFormulario(initial={'nombre':entregable.nombre, 'apellido':entregable.apellido, 'email':entregable.email, 'profesion':entregable.profesion})
    # Se renderiza la pagina de edicion.
    return render(request, 'editarEntregable.html', {'miFormulario':miFormulario, 'entregable_nombre':entregable_nombre})


def buscarEntregable(request):
    return render(request, 'buscarEntregable.html')

def encontrarEntregable(request):
    if request.GET['nombre']:
        nombre = request.GET['nombre']
        entregables = Entregable.objects.filter(nombre=nombre)
        return render(request, 'AppCoder/resultadosEntregable.html', {'nombre':nombre, 'entregables':entregables})
    else:
        respuesta = 'No se ingresó ningún entregable con ese nombre'
        return render(request, 'AppCoder/resultadosEntregable.html', {'respuesta':respuesta})


   

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


def editarProfesor (request, profesor_nombre):

# Recibe el nombre del profesor a editar.
    profesor = Profesor.objects.get(nombre=profesor_nombre)
    
# Si el metodo es POST, se realiza la edicion.
    if request.method == 'POST':
        miFormulario = ProfesorFormulario(request.POST)

        if miFormulario.is_valid(): # Si el formulario es valido, se guarda.
            informacion = miFormulario.cleaned_data
            
            profesor.nombre = informacion['nombre']
            profesor.apellido = informacion['apellido']
            profesor.email = informacion['email']
            profesor.profesion = informacion['profesion']            
            
            profesor.save()


            return render(request, 'AppCoder/inicio.html') # Se redirige a la pagina de inicio.
    # Si el metodo es GET, se muestra el formulario.
    else:
        miFormulario = ProfesorFormulario(initial={'nombre':profesor.nombre, 'apellido':profesor.apellido, 'email':profesor.email, 'profesion':profesor.profesion})
    # Se renderiza la pagina de edicion.
    return render(request, 'editarProfesor.html', {'miFormulario':miFormulario, 'profesor_nombre':profesor_nombre})


def buscarProfesor(request):
    return render(request, 'buscarProfesor.html')

def encontrarProfesor(request):
    if request.GET['nombre']:
        nombre = request.GET['nombre']
        profesores = Profesor.objects.filter(nombre=nombre)
        return render(request, 'AppCoder/resultadosProfesor.html', {'nombre':nombre, 'profesores':profesores})
    else:
        respuesta = 'No se ingresó ningún profesor con ese nombre'
        return render(request, 'AppCoder/resultadosProfesor.html', {'respuesta':respuesta})