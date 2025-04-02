from django.contrib import admin
from .models import Unidade, Local, Ocorrencia, DataAbertura, DataEncerramento, Comentario, Plantao


admin.site.register(Unidade)
admin.site.register(Local)
admin.site.register(Ocorrencia)
admin.site.register(DataAbertura)
admin.site.register(DataEncerramento)
admin.site.register(Comentario)
admin.site.register(Plantao)

