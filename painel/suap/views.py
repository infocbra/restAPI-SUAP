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
    template_name = "forms/form.html"
    fields = ['nome']
    success_url = reverse_lazy('registrar')


class StatusUpdate(UpdateView):
    model = models.StatusSenha
    template_name = 'forms/form.html'
    context_object_name = 'status'
    fields = ['nome']
    success_url = reverse_lazy('registrar')


class StatusDelete(DeleteView):
    model = models.StatusSenha
    template_name = 'registro.html'
    success_url = reverse_lazy('registrar')


class TipoCreate(CreateView):
    """Criando view para Tipo"""
    model = models.Tipo
    template_name = "forms/form.html"
    fields = ['nome']
    success_url = reverse_lazy('registrar')


class TipoUpdate(UpdateView):
    model = models.Tipo
    template_name = 'forms/form.html'
    context_object_name = 'status'
    fields = ['nome']
    success_url = reverse_lazy('registrar')


class TipoDelete(DeleteView):
    model = models.Tipo
    template_name = 'registro.html'
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
    """Criando view para Tipo"""
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
    template_name = "guiche/del_campus.html"
    success_url = reverse_lazy('registrar')


class AtendenteView(TemplateView):
    """Criando view para Tipo"""
    template_name = "forms/atendente.html"
    initial = {'key': 'value'}
    form_class = forms.AtendenteForm

    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            dados_form = form.data
            atendente = models.Atendente(Siape= dados_form['Siape'],Nome=dados_form['Nome'])
            atendente.save()
            return HttpResponseRedirect('/')
        return render(request, self.template_name, {'form':form})


class AtendimentoView(TemplateView):
    """Criando view para Tipo"""
    template_name = "atendimento.html"

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        return render(request, self.template_name)