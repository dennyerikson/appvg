from .models import *
from django import forms
from django.forms.widgets import Select   
from django.contrib.admin import widgets

class CandidatosForm(forms.ModelForm):
    class Meta:
        #criar choices com persistencia
        CURSOS = Cursos.objects.all()

        model = Candidatos
        fields = (
            'nome','email','data_nasc', 'data_hist', 'rg', 'cpf', 'tel', 'cel',
            'endereco', 'endereco_n', 'endereco_cep', 'endereco_cid', 'endereco_est',
            'curso_opc1', 'period_opc1', 'curso_opc2', 'period_opc2', 'opc_info'
        )

        widgets = {
            'curso_opc1':Select(choices=((choice.pk, choice.nome_curso) for choice in CURSOS )),
            'curso_opc2':Select(choices=((choice.pk, choice.nome_curso) for choice in CURSOS )),
        }