from django import forms
from .models import StatusSenha, Tipo, Categoria

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = StatusSenha
        fields = [
            'nome'
        ]


class TipoForm(forms.ModelForm):
    class Meta:
        model = Tipo
        fields = [
            'nome'
        ]

class StatusForm(forms.ModelForm):
    class Meta:
        model = StatusSenha
        fields = [
            'nome'
        ]