from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView
from .models import Ocorrencia
# Create your views here.


# Listar as Ocorrências

class CadastrarOcorrenciaView(CreateView):
    model = Ocorrencia
    form_class = Ocorrencia
    template_name = "ocorrencia/cadastrar_ocorrencia.html"
    success_url = reverse_lazy("lista_ocorrencia")
class ListaOcorrenciaView(ListView):
    model = Ocorrencia
    template_name = 'ocorrencia/lista_ocorrencia.html'
    context_object_name = 'ocorrencia'

# Mostrar os detalhes da ocorrencia
class DetalheOcorrenciaView(DetailView):
    model = Ocorrencia
    template_name = 'ocorrencia/detalhe_ocorrencia.html'
    context_object_name = 'ocorrencia'