from django import forms
from .models import Ocorrencia, Plantao, Comentario, Planta, Ativo
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
            'titulo', 'unidade', 'tipo_local', 
            'planta', 'ativo',
            'endereco', 'localizacao',
            'criticidade', 'status',
            'data_solicitacao', 'descricao'
        ]
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}), 
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
        ocorrencia = super().save(commit=False)
        from .models import LocalInterno, LocalExterno

        if self.cleaned_data['tipo_local'] == 'interno':
            if ocorrencia.local_interno:
                li = ocorrencia.local_interno
                li.planta = self.cleaned_data['planta']
                li.ativo = self.cleaned_data['ativo']
                li.save()
            else:
                li = LocalInterno.objects.create(
                    planta=self.cleaned_data['planta'],
                    ativo=self.cleaned_data['ativo']
                )
            ocorrencia.local_interno = li
            ocorrencia.local_externo = None

        else:
            if ocorrencia.local_externo:
                le = ocorrencia.local_externo
                le.nome = self.cleaned_data['endereco']
                le.localizacao = self.cleaned_data['localizacao']
                le.save()
            else:
                le = LocalExterno.objects.create(
                    nome=self.cleaned_data['endereco'],
                    localizacao=self.cleaned_data['localizacao']
                )
            ocorrencia.local_externo = le
            ocorrencia.local_interno = None
        if commit:
            ocorrencia.save()
        return ocorrencia
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        instance = kwargs.get('instance')
        tipo_local_val = ''

        if instance:
            if instance.local_interno:
                tipo_local_val = 'interno'
                self.fields['tipo_local'].initial = 'interno'
                self.fields['planta'].initial = instance.local_interno.planta
                self.fields['ativo'].initial = instance.local_interno.ativo
            elif instance.local_externo:
                tipo_local_val = 'externo'
                self.fields['tipo_local'].initial = 'externo'
                self.fields['endereco'].initial = instance.local_externo.nome
                self.fields['localizacao'].initial = instance.local_externo.localizacao

        # Adicionar o atributo data-initial ao widget do tipo_local
        self.fields['tipo_local'].widget.attrs['data-initial'] = tipo_local_val
   

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
       







