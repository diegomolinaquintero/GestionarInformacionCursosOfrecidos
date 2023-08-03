from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('VerDocente/', views.docente_list, name='docente_list'),
    path('DocenteDetalle/<int:pk>/', views.docente_detail, name='docente_detail'),
    path('DocenteEdit/<int:pk>/', views.docente_edit, name='docente_edit'),
    path('DocenteNuevo/', views.docente_new, name='docente_new'),
    path('Docentedelete/<int:pk>/', views.docente_delete, name='docente_delete'),
    path('Vercursos/', views.curso_list, name='curso_list'),
    path('CursoDetalle/<int:pk>/', views.curso_detail, name='curso_detail'),
    path('CursoEdit/<int:pk>/', views.curso_edit, name='curso_edit'),
    path('CursoNuevo/', views.curso_new, name='curso_new'),
    path('Cursodelete/<int:pk>/', views.curso_delete, name='curso_delete'),
    
]