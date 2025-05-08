from django.urls import path
from plantao_coi.views import lista_ocorrencia, cadastrar_ocorrencia,\
    editar_ocorrencia, excluir_ocorrencia, adicionar_comentario,\
    concluir_ocorrencia, iniciar_plantao, cancelar_ocorrencia

urlpatterns = [
    path('', lista_ocorrencia, name='lista_ocorrencia'),
    path('iniciar_plantao/', iniciar_plantao, name='iniciar_plantao'),
    path('cadastrar/', cadastrar_ocorrencia, name='cadastrar_ocorrencia'),
    path('editar/<int:ocorrencia_id>/', editar_ocorrencia, name='editar_ocorrencia'),
    path('excluir/<int:ocorrencia_id>/', excluir_ocorrencia, name='excluir_ocorrencia'),
    path('adicionar_comentario/', adicionar_comentario, name='adicionar_comentario'),
    path('concluir/<int:ocorrencia_id>/', concluir_ocorrencia, name='concluir_ocorrencia'),
    path('cancelar/<int:ocorrencia_id>/', cancelar_ocorrencia, name='cancelar_ocorrencia'),


]
