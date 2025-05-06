from django.contrib import admin
from .models import (
    Unidade, LocalExterno, Ocorrencia, DataSolicitacao,
    Comentario, Plantao, LocalInterno, Planta, Ativo
)

@admin.register(Unidade)
class UnidadeAdmin(admin.ModelAdmin):
    list_display = ('nome',)

@admin.register(LocalExterno)
class LocalAdmin(admin.ModelAdmin):
    list_display = ('nome', 'localizacao', 'endereco')

@admin.register(LocalInterno)
class LocalInternoAdmin(admin.ModelAdmin):
    list_display = ('planta', 'ativo')

@admin.register(Ocorrencia)
class OcorrenciaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'unidade', 'status', 'local_interno', 'data_solicitacao')
    list_filter = ('status', 'criticidade')
    search_fields = ('titulo', 'descricao')

@admin.register(DataSolicitacao)
class DataSolicitacaoAdmin(admin.ModelAdmin):
    list_display = ('data',)

@admin.register(Comentario)
class ComentarioAdmin(admin.ModelAdmin):
    list_display = ('user', 'ocorrencia', 'data_criacao')

@admin.register(Plantao)
class PlantaoAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'inicio', 'turno')

@admin.register(Planta)
class PlantaAdmin(admin.ModelAdmin):
    list_display = ('nome',)

@admin.register(Ativo)
class AtivoAdmin(admin.ModelAdmin):
    list_display = ('codigo',)



