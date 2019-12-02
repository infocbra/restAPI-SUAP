# render templates, telas de acesso
from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect

# models 
from api.models import Categoria, StatusSenha, Senha, Tipo, Guiche, Campus, Atendente

# forms 
from suap.forms import CategoriaForm, TipoForm, StatusForm, GuicheForm, CampusForm, AtendenteForm


class IndexView(TemplateView):
    """View da tela inicial"""
    template_name = "index.html"

    def get(self, request):
        return render(request, self.template_name, {'data': {
            'categoria': Categoria.objects.all(), 
            'status': StatusSenha.objects.all(),
            'tipo': Tipo.objects.all()
            }})


class CategoriaView(TemplateView):
    """Criando view para Categoria"""
    template_name = "categoria.html"
    initial = {'key':'value'}
    form_class = CategoriaForm

    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            dados_form = form.data
            categoria = Categoria(nome= dados_form['nome'])
            categoria.save()
            return HttpResponseRedirect('/')

        return render(request, self.template_name, {'form':form})


class StatusView(TemplateView):
    """Criando view para Status"""
    template_name = "status.html"
    initial = {'key': 'value'}
    form_class = StatusForm

    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            dados_form = form.data
            status = StatusSenha(nome= dados_form['nome'])
            status.save()
            return HttpResponseRedirect('/')
        return render(request, self.template_name, {'form': form})



class TipoView(TemplateView):
    """Criando view para Tipo"""
    template_name = "tipo.html"
    initial = {'key': 'value'}
    form_class = TipoForm

    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form})

    
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            dados_form = form.data
            tipo = Tipo(nome= dados_form['nome'])
            tipo.save()
            return HttpResponseRedirect('/')
        return render(request, self.template_name, {'form':form})

class GuicheView(TemplateView):
    """Criando view para Tipo"""
    template_name = "guiche.html"
    initial = {'key': 'value'}
    form_class = GuicheForm

    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            dados_form = form.data
            guiche = Guiche(num_guiche= dados_form['num_guiche'],status=dados_form['status'])
            guiche.save()
            return HttpResponseRedirect('/')
        return render(request, self.template_name, {'form':form})

class CampusView(TemplateView):
    """Criando view para Tipo"""
    template_name = "campus.html"
    initial = {'key': 'value'}
    form_class = CampusForm

    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            dados_form = form.data
            campus = Campus(Campo= dados_form['Campo'])
            campus.save()
            return HttpResponseRedirect('/')
        return render(request, self.template_name, {'form':form})

class AtendenteView(TemplateView):
    """Criando view para Tipo"""
    template_name = "atendente.html"
    initial = {'key': 'value'}
    form_class = AtendenteForm

    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            dados_form = form.data
            atendente = Atendente(Siape= dados_form['Siape'],Nome=dados_form['Nome'])
            atendente.save()
            return HttpResponseRedirect('/')
        return render(request, self.template_name, {'form':form})