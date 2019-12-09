# render templates, telas de acesso
from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from django.http import HttpResponseRedirect
from django.conf import settings
from django.urls import reverse_lazy

# models 
import api.models as models 

# forms 
import suap.forms as forms 


class IndexView(TemplateView):
    """View da tela inicial"""
    template_name = "index.html"


class RegistrarView(TemplateView):
    """View da tela inicial"""
    template_name = "public/registro.html"

    def get(self, request):
        return render(request, self.template_name, {'data': {
            'categoria': models.Categoria.objects.all(), 
            'status': models.StatusSenha.objects.all(),
            'tipo': models.Tipo.objects.all(),
            'guiche': models.Guiche.objects.all(),
            'campus': models.Campus.objects.all(),
            'atendente': models.Atendente.objects.all()
            }})

class DocsView(TemplateView):
    template_name = "public/docs.html"

class LoginView(TemplateView):
    template_name = "public/login.html"


class CategoriaCreate(CreateView):
    """Criando view para Categoria"""
    model = models.Categoria
    template_name = "categoria/nova_categoria.html"
    fields = ['nome']
    success_url = reverse_lazy('registrar')


class CategoriaUpdate(UpdateView):
    model = models.Categoria
    template_name = "categoria/up_categoria.html"
    context_object_name = 'categorias'
    fields = ['nome']
    success_url = reverse_lazy('registrar')


class CategoriaDelete(DeleteView):
    model = models.Categoria
    template_name = "categoria/del_categoria.html"
    context_object_name = 'categorias'
    success_url = reverse_lazy('registrar')


class StatusCreate(CreateView):
    """Criando view para Status"""
    model = models.StatusSenha
    template_name = "status/novo_status.html"
    fields = ['nome']
    success_url = reverse_lazy('registrar')


class StatusUpdate(UpdateView):
    model = models.StatusSenha
    template_name = 'status/up_status.html'
    context_object_name = 'status'
    fields = ['nome']
    success_url = reverse_lazy('registrar')


class StatusDelete(DeleteView):
    model = models.StatusSenha
    template_name = 'status/del_status.html'
    success_url = reverse_lazy('registrar')


class TipoCreate(CreateView):
    """Criando view para Tipo"""
    model = models.Tipo
    template_name = "tipo/novo_tipo.html"
    fields = ['nome']
    success_url = reverse_lazy('registrar')


class TipoUpdate(UpdateView):
    model = models.Tipo
    template_name = 'tipo/up_tipo.html'
    context_object_name = 'status'
    fields = ['nome']
    success_url = reverse_lazy('registrar')


class TipoDelete(DeleteView):
    model = models.Tipo
    template_name = 'tipo/del_tipo.html'
    success_url = reverse_lazy('registrar')


class GuicheCreate(CreateView):
    """Criando view para Tipo"""
    model = models.Guiche
    template_name = "guiche/novo_guiche.html"
    fields = ['num_guiche', 'status', 'campus']
    success_url = reverse_lazy('registrar')


class GuicheUpdate(UpdateView):
    model = models.Guiche
    template_name = "guiche/up_guiche.html"
    fields = ['num_guiche', 'status', 'campus']
    success_url = reverse_lazy('registrar')


class GuicheDelete(DeleteView):
    """Criando view para Tipo"""
    model = models.Guiche
    template_name = "guiche/del_guiche.html"
    success_url = reverse_lazy('registrar')


class CampusCreate(CreateView):
    """Criando view para Campus"""
    model = models.Campus
    template_name = "campus/novo_campus.html"
    fields = ['nome']
    success_url = reverse_lazy('registrar')


class CampusUpdate(UpdateView):
    model = models.Campus
    template_name = "campus/up_campus.html"
    fields = ['nome']
    success_url = reverse_lazy('registrar')


class CampusDelete(DeleteView):
    """Criando view para Tipo"""
    model = models.Campus
    template_name = "campus/del_campus.html"
    success_url = reverse_lazy('registrar')


class AtendenteCreate(CreateView):
    """Criando view para Campus"""
    model = models.Atendente
    template_name = "atendente/novo_atendente.html"
    fields = ['nome', 'siape']
    success_url = reverse_lazy('registrar')


class AtendenteUpdate(UpdateView):
    model = models.Atendente
    template_name = "atendente/up_atendente.html"
    fields = ['nome', 'siape']
    success_url = reverse_lazy('registrar')


class AtendenteDelete(DeleteView):
    """Criando view para Tipo"""
    model = models.Atendente
    template_name = "atendente/del_atendente.html"
    success_url = reverse_lazy('registrar')


class AtendimentoView(TemplateView):
    """Criando view para Tipo"""
    template_name = "public/atendimento.html"

    def get(self, request):
        return render(request, self.template_name)

class ChamarNovaSenhaView(TemplateView):
    """Criando view para Tipo"""
    template_name = "public/atendimento.html"

    def get(self, request):
        senha = models.Senha.objects.filter(status=models.StatusSenha.objects.get(nome='Na fila')).order_by('hora_data')[0]
        senha.status = models.StatusSenha.objects.get(nome ='Em atendimento')
        senha.save()
        return render(request, self.template_name, {'senha': senha})

class ChamarSenhaNovamenteView(TemplateView):
    """Criando view para Tipo"""
    template_name = "public/atendimento.html"

    def get(self, request, *args, **kwargs):
        senha = models.Senha.objects.get(id=self.kwargs['pk'])
        return render(request, self.template_name, {'senha': senha})

