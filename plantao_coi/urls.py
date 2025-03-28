from django.urls import path
from . import views

urlpatterns = [
    path('', views.ListaOcorrenciaView.as_view(), name='lista_ocorrencia'),
    path('detalhe/<int:id>/', views.DetalheOcorrenciaView.as_view(), name='detalhe_ocorrencia'),
]