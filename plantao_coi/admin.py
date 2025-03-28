from django.contrib import admin
from .models import Unidade, Local, Ocorrencia
# Register your models here.


@admin.register(Unidade)
class UnidadeAdmin(admin.ModelAdmin):
    list_display = ('nome',)

@admin.register(Local)
class LocalAdmin(admin.ModelAdmin):
    list_display = ('local',)

@admin.register(Ocorrencia)
class OcorrenciaAdmin(admin.ModelAdmin):
    list_display = ('unidade', 'titulo', 'local', 'status', 'data_abertura', 'data_encerramento')
    list_filter = ('status', 'unidade', 'local')
    search_fields = ('descricao', 'titulo__descricao', 'local__local')

