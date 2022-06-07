from django import forms

# ACA VAMOS A DETERMINAR CADA UNO DE LOS FORMULARIOS MEDIANTE LOS CUALES INGRESAREMOS LOS DISTINTOS OBJETOS A LA PAGINA. (SIGUE EN VIEWS.PY)

class CursoFormulario(forms.Form):
    curso = forms.CharField(max_length=50)
    comision = forms.IntegerField()

class ProfesorFormulario(forms.Form):
    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=40)
    email = forms.EmailField()
    profesion = forms.CharField(max_length=40)

class EstudianteFormulario(forms.Form):
    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=40)
    email = forms.EmailField()

class EntregableFormulario(forms.Form):
    nombre = forms.CharField(max_length=40)
    fecha_de_entrega = forms.DateField()
    entregado = forms.BooleanField()

