from django.urls import path
from .views import curso, formularioEntregable, formularioProfesor, inicio, entregable, estudiante, formularioEstudiante, cursoFormulario, buscar, busquedaDeComision, verProfesores, editarProfesor, eliminarProfesor, eliminarCurso, editarCurso, buscarEstudiante, encontrarEstudiante, eliminarEstudiante, editarEstudiante, buscarProfesor, encontrarProfesor, buscarEntregable, editarEntregable, eliminarEntregable, encontrarEntregable

# ESTE ES UN PASO DE VITAL IMPORTANCIA QUE PERMITIRA NOMBRAR CADA RUTA MEDIANTE LA CUAL ACCEDEREMOS A NUESTRAS VIEWS, TODA VIEW NECESITA TENER SU PATH PARA SER VISTA EN LA INTERFACE. 

urlpatterns = [
    # paths de paginas iniciales
    path('', inicio, name='Inicio'),

    # paths de paginas de cursos
    path('cursos/', curso, name= 'Cursos'),
    path('editarCurso/<nombre>', editarCurso, name = 'editarCurso'),
    path('eliminarCurso/<nombre>', eliminarCurso, name = 'eliminarCurso'),
    path('cursoFormulario/', cursoFormulario, name ='cursoFormulario'),
    path('BusquedaDeComision/', busquedaDeComision, name = 'BusquedaDeComision'	),
    path('Buscar/', buscar, name = 'Buscar'),

    # paths de paginas de entregables
    path('entregables/', entregable, name='Entregable'),
    path('FormularioEntregable/', formularioEntregable, name = 'FormularioEntregable'),  
    path('buscarEntregable/', buscarEntregable, name = 'buscarEntregable'	),
    path('encontrarEntregable/', encontrarEntregable, name = 'encontrarEntregable'	),
    path('eliminarEntregable/<nombre>', eliminarEntregable, name = 'eliminarEntregable'),
    path('editarEntregable/<nombre>', editarEntregable, name = 'editarEntregable'),  
    
    # paths de paginas de estudiantes
    path('estudiantes/', estudiante, name='Estudiante'),
    path('FormularioEstudiante/', formularioEstudiante, name='FormularioEstudiante'),
    path('buscarEstudiante/', buscarEstudiante, name = 'buscarEstudiante'	),
    path('encontrarEstudiante/', encontrarEstudiante, name = 'encontrarEstudiante'	),
    path('eliminarEstudiante/<nombre>', eliminarEstudiante, name = 'eliminarEstudiante'),
    path('editarEstudiante/<nombre>', editarEstudiante, name = 'editarEstudiante'),

    # paths de paginas de profesores
    path('FormularioProfesores/', formularioProfesor, name='FormularioProfesores'),
    path('editarProfesor/<profesor_nombre>', editarProfesor, name = 'editarProfesor'),
    path('Profesores/', verProfesores, name='Profesores'),
    path('eliminarProfesor/<nombre>', eliminarProfesor, name = 'eliminarProfesor'),
    path('buscarProfesor/', buscarProfesor, name = 'buscarProfesor'	),
    path('encontrarProfesor/', encontrarProfesor, name = 'encontrarProfesor'),
    
]   
