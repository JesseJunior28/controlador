from django.shortcuts import get_object_or_404, render, redirect, reverse
from .models import Ocorrencia, Plantao, Comentario, OcorrenciaLog
from .forms import OcorrenciaForm, ComentarioForm, OcorrenciaFilterForm, PlantaoForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from urllib.parse import urlencode
from datetime import time, datetime
# Create your views here.


# Listar as Ocorrências

@login_required
def lista_ocorrencia(request):

    agora = datetime.now().time()
    hoje = datetime.now().date()
    
    if time(6, 0) <= agora < time(18, 0):

        plantao = Plantao.objects.filter(inicio__date=hoje, turno=Plantao.TurnoPlantao.DIURNO).first()
    else:
        plantao = Plantao.objects.filter(inicio__date=hoje, turno=Plantao.TurnoPlantao.NOTURNO).first()

    print(plantao)
    if not plantao:
        messages.warning(request, f'Nenhum plantão iniciado, favor iniciar o plantão!')
        return redirect('iniciar_plantao')

    ocorrencias = Ocorrencia.objects.all()
    em_aberto = ocorrencias.filter(status=Ocorrencia.EM_ABERTO).count()
    form = OcorrenciaFilterForm(request.GET, initial={'status': Ocorrencia.EM_ABERTO})

    if request.GET.get('unidade'):
        ocorrencias = ocorrencias.filter(unidade=request.GET.get('unidade'))
    if request.GET.get('data_abertura'):
        ocorrencias = ocorrencias.filter(data_abertura=request.GET.get('data_abertura'))
    if request.GET.get('data_solicitacao'):
        ocorrencias = ocorrencias.filter(data_solicitacao=request.GET.get('data_solicitacao'))
    if request.GET.get('status', Ocorrencia.EM_ABERTO):
        status = request.GET.get('status', Ocorrencia.EM_ABERTO)
        ocorrencias = ocorrencias.filter(status=status)
 
    
    
    context = {
        "ocorrencias": ocorrencias,
        "plantao": plantao,
        'form': form,
        'em_aberto': em_aberto,
        'ocorrencia_id': int(request.GET.get('ocorrencia_id', '0'))
    }
    
    return render(request, "ocorrencia/lista_ocorrencia.html", context)

@login_required
def cadastrar_ocorrencia(request):

    agora = datetime.now().time()
    hoje = datetime.now().date()
    
    if time(6, 0) <= agora < time(18, 0):
        plantao = Plantao.objects.filter(inicio__date=hoje, turno=Plantao.TurnoPlantao.DIURNO).first()
    else:
        plantao = Plantao.objects.filter(inicio__date=hoje, turno=Plantao.TurnoPlantao.NOTURNO).first()

    if not plantao:
        messages.warning(request, f'Nenhum plantão iniciado, favor iniciar o plantão!')
        return redirect('iniciar_plantao')
    

    if request.method == "POST":
        form = OcorrenciaForm(request.POST)
        if form.is_valid():
            ocorrencia = form.save()
            OcorrenciaLog.objects.create(usuario=request.user, acao=OcorrenciaLog.CRIAR, ocorrencia=ocorrencia)
            messages.success(request, f'Ocorrência {ocorrencia.id} cadastrada com sucesso!')
            return redirect("lista_ocorrencia")
    else:
        form = OcorrenciaForm(initial={'plantonista': request.user, 'plantao': plantao})
        
    return render(request, "ocorrencia/cadastrar_ocorrencia.html", {"form": form})

def editar_ocorrencia(request, ocorrencia_id):
    ocorrencia = get_object_or_404(Ocorrencia, id=ocorrencia_id)
    if request.method == 'POST':
        form = OcorrenciaForm(request.POST, instance=ocorrencia)
        if form.is_valid():
            form.save()
            OcorrenciaLog.objects.create(usuario=request.user, acao=OcorrenciaLog.EDITAR, ocorrencia=ocorrencia)
            messages.success(request, f'Ocorrência {ocorrencia.id} editada com sucesso!')
            return redirect('lista_ocorrencia')
    else:
        form = OcorrenciaForm(instance=ocorrencia)
    return render(request, 'ocorrencia/editar_ocorrencia.html', {'form': form})


def excluir_ocorrencia(request, ocorrencia_id):
    ocorrencia = get_object_or_404(Ocorrencia, id=ocorrencia_id)
    ocorrencia.delete()
    messages.warning(request, f'Ocorrência excluída com sucesso!')
    return redirect('lista_ocorrencia')


def adicionar_comentario(request):
    try:
        ocorrencia_id = request.POST.get('ocorrencia')
        texto = request.POST.get('texto')
        
        if not ocorrencia_id or not texto:
            return JsonResponse({
                'status': 'error',
                'message': 'Dados incompletos'
            })
            
        ocorrencia = get_object_or_404(Ocorrencia, id=ocorrencia_id)
        
        Comentario.objects.create(
            ocorrencia=ocorrencia,
            user=request.user,
            texto=texto
        )
        OcorrenciaLog.objects.create(
            usuario=request.user,
            acao=OcorrenciaLog.COMENTAR,
            ocorrencia=ocorrencia
        )
        
        return JsonResponse({
            'status': 'success',
            'message': 'Comentário adicionado com sucesso'
        })
    except Exception as e:
        return JsonResponse({
            'status': 'error',
            'message': str(e)
        })



def concluir_ocorrencia(request, ocorrencia_id):
    ocorrencia = get_object_or_404(Ocorrencia, pk=ocorrencia_id)

    ocorrencia.status = Ocorrencia.CONCLUIDA
    ocorrencia.save()
    OcorrenciaLog.objects.create(
        usuario=request.user,
        acao=OcorrenciaLog.CONCLUIR,
        ocorrencia=ocorrencia
    )
    messages.success(request, f'Ocorrência {ocorrencia.id} concluída com sucesso!')
    
    return redirect('lista_ocorrencia')

def cancelar_ocorrencia(request, ocorrencia_id):
    ocorrencia = get_object_or_404(Ocorrencia, pk=ocorrencia_id)

    ocorrencia.status = Ocorrencia.CANCELADA
    ocorrencia.save()
    comentario = Comentario(
        ocorrencia=ocorrencia,
        texto=request.POST.get('comentario',''),
        user=request.user
    )
    comentario.save()
    OcorrenciaLog.objects.create(
        usuario=request.user,
        acao=OcorrenciaLog.CANCELAR,
        ocorrencia=ocorrencia,
    )
    messages.success(request, 'Ocorrência {} cancelada com sucesso!'.format(ocorrencia.id))
    
    return redirect('lista_ocorrencia')

@login_required
def iniciar_plantao(request):
    if request.method == 'POST':
        form = PlantaoForm(request.POST)
        if form.is_valid():
            plantao = form.save(commit=False)
            plantao.usuario = request.user
            plantao.save()
            messages.success(request,"Plantao iniciado com sucesso!")
        return redirect('lista_ocorrencia')
    return render(request, 'ocorrencia/plantao.html')