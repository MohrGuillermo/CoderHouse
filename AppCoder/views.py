
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView # SE IMPORTAN LAS CLASES DE LA LIBRERIA GENERICA
from django.http import HttpResponse 
from django.shortcuts import render 
from django.urls import reverse_lazy 
from AppCoder.models import Curso, Estudiante, Profesor, Entregable 
from AppCoder.forms import CursoFormulario, ProfesorFormulario, EstudianteFormulario, EntregableFormulario
#LOGIN
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate, logout
 
#  ACA ES DONDE VAMOS A CREAR REALMENTE LOS FORMULARIOS MEDIANTE EL API DE DJANGO, ES DECIR, UNA HERRAMIENTA QUE PERMITE HACER MUCHO MAS FACIL Y DINAMICA LA CREACION DE FORMULARIOS, YA QUE UNA VEZ DETERMINADA LA CLASE EN FORMS.PY NO HARA FALTA NOMBRAR CADA UNA DE LAS VARIABLES A AGREGAR DESPUES. (SIGUE EN URLS.PY)

def inicio(request):
    return render(request, 'Inicio.html')

#Vamos a usar las vistas de "cursos" para mostrar como se harian todos estos CRUDS mediante los LISTVIEWS de Django.


#LISTVIEWS DE CURSOS
class CursoList(ListView): # SE CREA UNA CLASE PARA MOSTRAR TODOS LOS Cursos
    model = Curso # SE LE ASIGNA EL MODELO Curso
    template_name = 'AppCoder/curso_list.html' # SE LE ASIGNA EL NOMBRE DEL TEMPLATE

class CursoDetalle(DetailView): # SE CREA UNA CLASE PARA MOSTRAR UN CURSO
    model = Curso
    template_name = 'AppCoder/curso_detalle.html'

class CursoCreacion(CreateView): # SE CREA UNA CLASE PARA CREAR UN Curso
    model = Curso # SE LE ASIGNA EL MODELO Curso
    fields = ['nombre', 'comision']  # SE LE ASIGNA LOS CAMPOS QUE VA A TENER EL FORMULARIO
    success_url = reverse_lazy('cursos_listar') # SE LE ASIGNA LA URL QUE VA A IR AL USUARIO CUANDO SE CREE UN Curso
    
class CursoEdicion(UpdateView): # Clase que permite editar un Curso.
    model = Curso # Se le asigna el modelo Curso
    fields = ['nombre', 'comision']  # Se le asigna los campos que va a tener el formulario
    success_url = reverse_lazy('cursos_listar') # Se le asigna la url que va a ir al usuario cuando se edite un Curso

class CursoEliminacion(DeleteView): # Clase que permite eliminar un Curso.
    model = Curso # Se le asigna el modelo Curso
    success_url = reverse_lazy('cursos_listar') # Se le asigna la url que va a ir al usuario cuando se elimine un Curso

#ESTAS VISTAS SON VIEJAS PERO TODAVIA NO LAS HICIMOS

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



#Lo siguiente entonces queda comentado, pero no pierde validez, simplemente mostramos otra manera mejor y mas rapida de hacerlo que requiere menos codigo.


# def curso(request):
#     lista_cursos = Curso.objects.all()
#     return render(request, 'AppCoder/template_cursos.html', {'lista_cursos':lista_cursos})



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
            
# def cursoFormulario(request):
#     if request.method == 'POST':
#         miFormulario = CursoFormulario(request.POST)
#         if miFormulario.is_valid():
#             informacion = miFormulario.cleaned_data
#             nombre = informacion['curso']
#             comision = informacion['comision']
#             curso = Curso(nombre=nombre, comision=comision)
#             curso.save()
#             return render(request, 'AppCoder/Inicio.html')
#     else:
#         miFormulario= CursoFormulario()



# ESTUDIANTES
def estudiante(request):
    estudiantes = Estudiante.objects.all()
    return render(request, 'template_estudiantes.html' , {'estudiantes':estudiantes})  # ACA SE PASA UN DICCIONARIO A LA VISTA, PARA QUE LA VISTA PUEDA ACCEDER A LOS DATOS
def formularioEstudiante(request):
    if request.method == 'POST': # ACA SE VERIFICA SI EL METODO ES POST, PORQUE SI ES POST, SE GUARDAN LOS DATOS EN LA BASE DE DATOS
        miFormulario = EstudianteFormulario(request.POST) # ACA SE CREA UN FORMULARIO CON LOS DATOS QUE SE INGRESARON EN EL FORMULARIO
        if miFormulario.is_valid(): # ACA SE VERIFICA SI EL FORMULARIO ES VALIDO, PORQUE SI ES VALIDO, SE GUARDAN LOS DATOS EN LA BASE DE DATOS
            informacion = miFormulario.cleaned_data 
            nombre = informacion['nombre']
            apellido = informacion['apellido']
            email = informacion['email']
            estudiante = Estudiante(nombre=nombre, apellido=apellido, email=email) # ACA SE CREA UN OBJETO DE LA CLASE ESTUDIANTE, Y SE LE ASIGNA LOS DATOS QUE SE INGRESARON EN EL FORMULARIO
            estudiante.save() # ACA SE GUARDA EL OBJETO EN LA BASE DE DATOS
            return render(request, 'AppCoder/Inicio.html') # ACA SE REDIRECCIONA A LA PAGINA INICIAL
    else:
        miFormulario = EstudianteFormulario()     # ACA SE CREA UN FORMULARIO VACIO
    return render(request, 'FormularioEstudiante.html', {'miFormulario':miFormulario}) # ACA SE PASA EL FORMULARIO A LA VISTA


def buscarEstudiante(request):
    return render(request, 'buscarEstudiante.html')   # ACA SE CREA UNA VISTA PARA BUSCAR UN ESTUDIANTE

def encontrarEstudiante(request): # ACA SE CREA UNA FUNCION PARA BUSCAR UN ESTUDIANTE
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
    estudiante = Estudiante.objects.get(nombre=nombre) # ACA SE OBTIENE EL ESTUDIANTE QUE SE QUIERE EDITAR
    if request.method == 'POST': # ACA SE VERIFICA SI EL METODO ES POST, PORQUE SI ES POST, SE GUARDAN LOS DATOS EN LA BASE DE DATOS
        miFormulario = EstudianteFormulario(request.POST) # ACA SE CREA UN FORMULARIO CON LOS DATOS QUE SE INGRESARON EN EL FORMULARIO
        if miFormulario.is_valid: # ACA SE VERIFICA SI EL FORMULARIO ES VALIDO, PORQUE SI ES VALIDO, SE GUARDAN LOS DATOS EN LA BASE DE DATOS
            informacion = miFormulario.cleaned_data # ACA SE OBTIENEN LOS DATOS QUE SE INGRESARON EN EL FORMULARIO
            estudiante.nombre = informacion['nombre'] 
            estudiante.apellido = informacion['apellido']
            estudiante.email = informacion['email']
            estudiante.save() # ACA SE GUARDA EL OBJETO EN LA BASE DE DATOS
            return render(request, 'AppCoder/inicio.html') # SE REDIRECCIONA A LA PAGINA INICIAL
    else:
        miFormulario = EstudianteFormulario(initial={'nombre':estudiante.nombre, 'apellido':estudiante.apellido, 'email':estudiante.email}) # ACA SE CREA UN FORMULARIO VACIO
    return render(request, 'editarEstudiante.html', {'miFormulario':miFormulario, 'nombre':nombre}) # ACA SE PASA EL FORMULARIO A LA VISTA




#ENTREGABLES

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


   
#profesores

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
            informacion = miFormulario.cleaned_data # Se obtiene la informacion del formulario.
            profesor.nombre = informacion['nombre']
            profesor.apellido = informacion['apellido']
            profesor.email = informacion['email']
            profesor.profesion = informacion['profesion']            
            profesor.save() # Se guarda.
            return render(request, 'AppCoder/inicio.html') # Se redirige a la pagina de inicio.
    # Si el metodo es GET, se muestra el formulario.
    else:
        miFormulario = ProfesorFormulario(initial={'nombre':profesor.nombre, 'apellido':profesor.apellido, 'email':profesor.email, 'profesion':profesor.profesion})
    # Se renderiza la pagina de edicion.
    return render(request, 'editarProfesor.html', {'miFormulario':miFormulario, 'profesor_nombre':profesor_nombre})

def buscarProfesor(request): # Funcion que muestra la pagina de busqueda.
    return render(request, 'buscarProfesor.html') 

def encontrarProfesor(request): # Funcion que busca un profesor.
    if request.GET['nombre']: # Si se ingreso un nombre.
        nombre = request.GET['nombre'] # Se obtiene el nombre.
        profesores = Profesor.objects.filter(nombre=nombre) # Se busca el profesor.
        return render(request, 'AppCoder/resultadosProfesor.html', {'nombre':nombre, 'profesores':profesores}) # Se muestra el resultado.
    else: # Si no se ingreso ningun nombre.
        respuesta = 'No se ingresó ningún profesor con ese nombre' # Se muestra un mensaje.
        return render(request, 'AppCoder/resultadosProfesor.html', {'respuesta':respuesta}) # Se muestra el resultado.

#----------------------------------------------
#LOGIN

def login_request(request):
    if request.method == 'POST': # Si el metodo es POST.
        form = AuthenticationForm(request,request.POST) # Se crea el formulario.
        if form.is_valid(): # Si el formulario es valido.
            usuario = request.POST['username'] # Se obtiene el usuario.
            clave = request.POST['password'] # Se obtiene la clave.
            autentificacion = authenticate(username=usuario, password=clave) # Se autentifica.
            if autentificacion is not None: # Si el usuario es valido.
                login(request, autentificacion) # Se logea.
                return render(request, 'AppCoder/Inicio.html', {'usuario':usuario, 'mensaje': f'Bienvenido {usuario}'}) # Se redirige a la pagina de Inicio.html.
            else: # Si el usuario no es valido.
                return render(request, 'AppCoder/Inicio.html', {'mensaje':'Usuario o contraseña incorrectos'}) # Se muestra un mensaje.
        else: # Si el formulario no es valido.
            return render(request, 'AppCoder/Inicio.html', {'mensaje':'Error formulario invalido'}) # Se muestra un mensaje.
    else: # Si el metodo es GET.
        form = AuthenticationForm() # Se crea el formulario.
        return render(request, 'AppCoder/login.html', {'form':form}) # Se muestra la pagina de login.

#REGISTRO
def registro_request(request): # Funcion que muestra la pagina de registro.
    if request.method == 'POST': # Si el metodo es POST.
        form = UserCreationForm(request.POST) # Se crea el formulario.
        if form.is_valid(): # Si el formulario es valido.
            username = form.cleaned_data['username'] # Se obtiene el nombre de usuario.
            form.save() # Se guarda.
            return render(request, 'AppCoder/Inicio.html', {'mensaje': f'Usuario "{username}" creado con éxito'}) # Se redirige a la pagina de Inicio.html.
        else: # Si el formulario no es valido.
            return render(request, 'AppCoder/Inicio.html', {'mensaje': 'No fue posible crear el usuario'}) # Se muestra un mensaje.
    else: # Si el metodo es GET.
        form = UserCreationForm() # Se crea el formulario.
        return render(request, 'AppCoder/registro.html', {'form':form}) # Se muestra la pagina de registro con el formulario.

# def registro(request):
#   if request.method == 'POST': # Si es POST, entonces es un formulario que viene lleno
#     form = UserCreationForm(request.POST)
#     if form.is_valid():
#       username = form.cleaned_data['username']
#       form.save()
#       return render(request, 'AppCoder/inicio.html', {'mensaje': f'Usuario {username} creado correctamente'})
#     else:
#       return render(request, 'AppCoder/inicio.html', {'mensaje': 'Error, no se pudo crear el usuario'})
#   else:
#     form = UserCreationForm()
#     return render(request, 'AppCoder/registro.html', {'form': form}) 