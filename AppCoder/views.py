from django.template import loader
from django.shortcuts import render
from AppCoder.models import Curso, Entregable, Estudiante, Profesor
 

def mi_plantilla(request):
    return render(request, 'plantilla.html')

def curso(request):
    curso = Curso(nombre = 'Javascript', comision = 12345)
    curso.save()
    dic = {'Nombre del curso:':curso.nombre, 'Camada N°: ':curso.comision}
    return render(request, 'template_cursos.html', dic)

def profesores(request):
    profesor_1= Profesor(nombre='Juan', apellido='Perez', email='juanperez@outlook.com', profesion='Ingeniero')
    profesor_1.save()
    dic= {'Nombre: ': profesor_1.nombre, 'Apellido: ': profesor_1.apellido, 'E-mail: ': profesor_1.email, 'Profesion: ': profesor_1.profesion}
    return render(request, 'template_profesores.html', dic)

def entregable(request):
    entregable_1=Entregable(nombre='TP_1', fecha_de_entrega=None, entregado=False)
    entregable_1.save()
    dic={'Nombre: ':entregable_1.nombre, 'Fecha de entrega: ':entregable_1.fecha_de_entrega, 'Estado: ':entregable_1.entregado}
    return render(request, 'template_entregables.html', dic)  

def estudiante(request):
    estudiante_1=Estudiante(nombre='Roberto', apellido='Dominguez', email='Robertodominguez@outlook.com')
    estudiante_1.save()
    dic={'Nombre: ':estudiante_1.nombre, 'Apellido: ':estudiante_1.apellido, 'E-mail: ':estudiante_1.email}
    return render(request, 'template_estudiantes.html', dic)  

