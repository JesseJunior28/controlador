from django.views.generic import ListView, DetailView
from .models import Ocorrencia
# Create your views here.


# Listar as Ocorrências
class ListaOcorrenciaView(ListView):
    model = Ocorrencia
    template_name = 'ocorrencia/lista_ocorrencia.html'
    context_object_name = 'ocorrencia'

# Mostrar os detalhes da ocorrencia
class DetalheOcorrenciaView(DetailView):
    model = Ocorrencia
    template_name = 'ocorrencia/detalhe_ocorrencia.html'
    context_object_name = 'ocorrencia'