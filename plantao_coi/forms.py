from django import forms
from .models import Ocorrencia, Comentario
from django.contrib.admin.widgets import AdminDateWidget

class OcorrenciaForm(forms.ModelForm):
    class Meta: 
        model = Ocorrencia
        fields = ['unidade', 'local', 'criticidade', 'titulo', 'descricao', 'status', 'data_encerramento']
        widgets = {
            'data_encerramento': forms.DateTimeBaseInput(attrs={'type': 'datetime-local'}),
            'descricao': forms.Textarea(attrs={'rows':4}),
        }


class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['texto']
        widgets = {
            'texto': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Adicione um comentário...'}),
        }



