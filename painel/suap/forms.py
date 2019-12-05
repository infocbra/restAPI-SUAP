from django import forms
import api.models as models

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = models.Categoria
        fields = [
            'nome'
        ]

class TipoForm(forms.ModelForm):
    class Meta:
        model = models.Tipo
        fields = [
            'nome'
        ]

class StatusForm(forms.ModelForm):
    class Meta:
        model = models.StatusSenha
        fields = [
            'nome'
        ]

class GuicheForm(forms.ModelForm):
    class Meta:
        model = models.Guiche
        fields = [
            'num_guiche',
            'status', 
            'campus',
        ]

class CampusForm(forms.ModelForm):
    class Meta:
        model = models.Campus
        fields = [
            'nome'
        ]

class AtendenteForm(forms.ModelForm):
    class Meta:
        model = models.Atendente
        fields = [
            'siape','nome'
        ]
