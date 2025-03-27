from django.shortcuts import render, get_object_or_404
from .models import Ocorrencia
# Create your views here.


# Listar as Ocorrências
def lista_ocorrencia(request):
    ocorrencias = Ocorrencia.objects.all()
    return render(request, 'ocorrencia/lista_ocorrencia.html', {'ocorrencia': ocorrencia})

# Mostrar os detalhes da ocorrencia
def detalhe_ocorrencia(request, id):
    ocorrencia = get_object_or_404(Ocorrencia, id=id)
    return render(request, 'ocorrencia/detalhe_ocorrencia.html', {'ocorrencia': ocorrencia})

