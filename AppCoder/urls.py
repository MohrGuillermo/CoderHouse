from django.urls import path
from .views import curso, formularioEntregable, formularioProfesor, inicio, entregable, estudiante, formularioEstudiante, cursoFormulario, buscar, busquedaDeComision, verProfesores, eliminarProfesor

# ESTE ES UN PASO DE VITAL IMPORTANCIA QUE PERMITIRA NOMBRAR CADA RUTA MEDIANTE LA CUAL ACCEDEREMOS A NUESTRAS VIEWS, TODA VIEW NECESITA TENER SU PATH PARA SER VISTA EN LA INTERFACE. 

urlpatterns = [
    # paths de paginas iniciales
    path('', inicio, name='Inicio'),
    path('cursos/', curso, name= 'Cursos'),
    path('Profesores/', verProfesores, name='Profesores'),
    path('entregables/', entregable, name='Entregable'),
    path('estudiantes/', estudiante, name='Estudiante'),
    # paths de formularios
    path('FormularioEstudiante/', formularioEstudiante, name='FormularioEstudiante'),
    path('FormularioProfesores/', formularioProfesor, name='FormularioProfesores'),
    path('cursoFormulario/', cursoFormulario, name ='cursoFormulario'),
    path('FormularioEntregable/', formularioEntregable, name = 'FormularioEntregable'),
    # paths de busqueda
    path('BusquedaDeComision/', busquedaDeComision, name = 'BusquedaDeComision'	),
    path('Buscar/', buscar, name = 'Buscar'),
    path('eliminarProfesor/<nombre>', eliminarProfesor, name = 'eliminarProfesor'),
]   
