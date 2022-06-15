from django.urls import path
from .views import inicio, formularioEntregable, formularioProfesor, entregable, estudiante, formularioEstudiante, verProfesores, editarProfesor, eliminarProfesor, buscarEstudiante, encontrarEstudiante, eliminarEstudiante, editarEstudiante, buscarProfesor, encontrarProfesor, buscarEntregable, editarEntregable, eliminarEntregable, encontrarEntregable, login_request, registro_request
# VISTAS DESCARTADAS Y REEMPLAZADAS POR LAS LISVIEWS DE DJANGO:curso, cursoFormulario, eliminarCurso, editarCurso,
# Vistas de busqueda de cursos que todavia no modificamos
from .views import buscar, busquedaDeComision
from .views import CursoCreacion, CursoEdicion, CursoEliminacion, CursoDetalle, CursoList # Importamos las vistas de las nuevas clases que creamos con Django LIST VIEWS.

# ESTE ES UN PASO DE VITAL IMPORTANCIA QUE PERMITIRA NOMBRAR CADA RUTA MEDIANTE LA CUAL ACCEDEREMOS A NUESTRAS VIEWS, TODA VIEW NECESITA TENER SU PATH PARA SER VISTA EN LA INTERFACE. 

urlpatterns = [
    # path de paginas iniciales
    path('', inicio, name='Inicio'),

    # paths de logueo de usuarios
    path('login/', login_request, name='login'),
    path('registro/', registro_request, name='registro'),

    # # paths de paginas de cursos, usando formularios basicos.
    # path('cursos/', curso, name= 'Cursos'),
    # path('editarCurso/<nombre>', editarCurso, name = 'editarCurso'),
    # path('eliminarCurso/<nombre>', eliminarCurso, name = 'eliminarCurso'),
    # path('cursoFormulario/', cursoFormulario, name ='cursoFormulario'),


    # Paths de paginas de cursos usando formularios de django

    path('cursos/list/', CursoList.as_view(), name='cursos_listar'),
    path('curso/<pk>', CursoDetalle.as_view(), name='curso_detalle'),
    path('curso/nuevo/', CursoCreacion.as_view(), name='curso_crear'),
    path('curso/editar/<pk>', CursoEdicion.as_view(), name='curso_editar'),
    path('curso/borrar/<pk>', CursoEliminacion.as_view(), name='curso_borrar'),
    
    # Paths de busqueda que todavia no modificamos
    path('Buscar/', buscar, name='Buscar'),
    path('busquedaDeComision/', busquedaDeComision, name='busquedaDeComision'),

    
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
