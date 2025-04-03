from django.contrib import admin
from .models import Unidade, Local, Ocorrencia, DataSolicitacao, Comentario, Plantao


admin.site.register(Unidade)
admin.site.register(Local)
admin.site.register(Ocorrencia)
admin.site.register(DataSolicitacao)
admin.site.register(Comentario)
admin.site.register(Plantao)

