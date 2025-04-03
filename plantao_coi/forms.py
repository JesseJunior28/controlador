from django import forms
from .models import Ocorrencia , Plantao, Comentario, DataSolicitacao
from django.contrib.admin.widgets import AdminDateWidget

class OcorrenciaForm(forms.ModelForm):
    class Meta: 
        model = Ocorrencia
        fields = ['unidade', 'local', 'criticidade', 'status', 'data_solicitacao']
        widgets = {
            "unidade": forms.Select(attrs={'class': 'form-control'}),
            "local": forms.Select(attrs={'class': 'form.control'}),
            "criticidade": forms.Select(attrs={'class': 'form.control'}),
            "status": forms.Select(attrs={'class': 'form.control'}),
            "data_solicitacao": forms.TextInput(attrs={'class': 'datetime-local', 'type': 'date'}),
            
        }

    def __init__(self, *args, **kwargs):
        super(OcorrenciaForm, self). __init__(*args, **kwargs)
        self.fields['unidade'].required = False
        self.fields['local'].empty_label = 'local'
        self.fields['local'].required = False
        self.fields['criticidade'].required = False
        self.fields['status'].empty_label = 'Status da Ocorência'
        self.fields['status'].required = False
        
class ComentarioForm(forms.ModelForm):
    
    class Meta:
        model = Comentario
        fields = ['texto', 'user', 'ocorrencia']

class PlantaoForm(forms.ModelForm):
    
    class Meta:
        model = Plantao
        fields = ['turno', 'inicio']
        widgets = {
            "turno": forms.Select(attrs={'class': 'form-control'}),
            "inicio": forms.TextInput(attrs={'class': 'form-control', 'type': 'datetime-' })

}

class DataSolicitacaoForm(forms.ModelForm):
    class Meta:
        model = DataSolicitacao
        fields = '__all__'
        widgets = {
            'data_de_solicitacao': AdminDateWidget()
        }
        
        




