from django.urls import path
from .views import curso, profesores, entregable, estudiante, mi_plantilla

urlpatterns = [
    path('curso/', curso),
    path('profesores/', profesores),
    path('entregables/', entregable),
    path('estudiantes/', estudiante),
    path('mi_plantilla/', mi_plantilla),
]   
