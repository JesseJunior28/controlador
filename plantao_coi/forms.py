from django import forms
from .models import Ocorrencia, Plantao, Comentario, DataSolicitacao, LocalInterno, Planta, Ativo
from django.contrib.admin.widgets import AdminDateWidget

class OcorrenciaForm(forms.ModelForm):
    TIPO_CHOICES = [
        ('interno', 'Local Interno'),
        ('externo', 'Local Externo'),
    ]

    tipo_local = forms.ChoiceField(
        choices=TIPO_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'}),
        label="Tipo de Local",
        required=True
    )

    # campos para "Interno"
    planta = forms.ModelChoiceField(
        queryset=Planta.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}),
        required=False
    )
    ativo = forms.ModelChoiceField(
        queryset=Ativo.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}),
        required=False
    )

    # campos para "Externo"
    endereco = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        required=False
    )
    localizacao = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        required=False
    )

    class Meta:
        model = Ocorrencia
        fields = [
            'unidade', 'tipo_local',
            'planta', 'ativo',
            'endereco', 'localizacao',
            'criticidade', 'status',
            'data_solicitacao', 'descricao'
        ]
        widgets = {
            'unidade': forms.Select(attrs={'class': 'form-control'}),
            'criticidade': forms.Select(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'data_solicitacao': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }

    def clean(self):
        cd = super().clean()
        tipo = cd.get('tipo_local')
        if tipo == 'interno':
            if not cd.get('planta') or not cd.get('ativo'):
                raise forms.ValidationError("Para Local Interno, informe Planta e Ativo.")
        else:  # externo
            if not cd.get('endereco') or not cd.get('localizacao'):
                raise forms.ValidationError("Para Local Externo, informe Endereço e Localização.")
        return cd

    def save(self, commit=True):
        # 1) salva a ocorrência sem local ainda
        ocorrencia = super().save(commit=False)

        # 2) com base no tipo, crie ou recupere o LocalInterno/LocalExterno
        from .models import LocalInterno, LocalExterno

        if self.cleaned_data['tipo_local'] == 'interno':
            li = LocalInterno.objects.create(
                planta=self.cleaned_data['planta'],
                ativo=self.cleaned_data['ativo']
            )
            ocorrencia.local_interno = li
            ocorrencia.local_externo = None
        else:
            le = LocalExterno.objects.create(
                nome="Externo",  # ou outro valor fixo
                localizacao=self.cleaned_data['localizacao'],
                endereco=self.cleaned_data['endereco']
            )
            ocorrencia.local_externo = le
            ocorrencia.local_interno = None

        if commit:
            ocorrencia.save()
        return ocorrencia


class PlantaoForm(forms.ModelForm):
    class Meta:
        model = Plantao
        fields = ['turno', 'inicio']
        widgets = {
            "turno": forms.Select(attrs={'class': 'form-control'}),
            "inicio": forms.TextInput(attrs={'class': 'datetime-local', 'type': 'datetime-local'})
        }

class OcorrenciaFilterForm(forms.ModelForm):
    class Meta: 
        model = Ocorrencia
        fields = ['unidade', 'local_interno', 'criticidade', 'status', 'data_solicitacao']
        widgets = {
            "unidade": forms.Select(attrs={'class': 'form-control'}),
            "local_interno": forms.Select(attrs={'class': 'form-control'}),
            "criticidade": forms.Select(attrs={'class': 'form-control'}),
            "status": forms.Select(attrs={'class': 'form-control'}),
            "data_solicitacao": forms.TextInput(attrs={'class': 'datetime-local', 'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super(OcorrenciaFilterForm, self).__init__(*args, **kwargs)
        self.fields['unidade'].required = False
        self.fields['local_interno'].empty_label = 'Local Interno'
        self.fields['local_interno'].required = False
        self.fields['criticidade'].required = False
        self.fields['status'].empty_label = 'Status da Ocorrência'
        self.fields['status'].required = False

class ComentarioForm(forms.ModelForm):
    
    class Meta:
        model = Comentario
        fields = ['texto', 'user', 'ocorrencia']

class DataSolicitacaoForm(forms.ModelForm):
    class Meta:
        model = DataSolicitacao
        fields = '__all__'
        widgets = {
            'data_de_solicitacao': AdminDateWidget()
        }






