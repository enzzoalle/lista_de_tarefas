from django.urls import path
from . import views
from django.conf.urls import handler404

handler404 = 'core.views.erro_404'

urlpatterns = [
    path('', views.index, name='index'),
    path('materias', views.materias, name='materias'),
    path('materias/<materia_id>', views.materia, name='materia'),
    path('nova_materia', views.nova_materia, name='nova_materia'),
    path('novo_comentario/<materia_id>', views.novo_comentario, name='novo_comentario'),
    path('editar_comentario/<comentario_id>', views.editar_comentario, name='editar_comentario'),
    path('materias/<materia_id>/excluir', views.excluir_materia, name='excluir_materia'),
    path('materias/excluir/<comentario_id>', views.excluir_comentario, name='excluir_comentario'),
]