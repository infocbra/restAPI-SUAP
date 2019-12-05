# render templates, telas de acesso
from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.utils import timezone
#from django.conf import settings

# models 
from api.models import Categoria, StatusSenha, Senha, Tipo, Guiche, Campus, Atendente, Atendimento

# forms 
from suap.forms import CategoriaForm, TipoForm, StatusForm, GuicheForm, CampusForm, AtendenteForm


class IndexView(TemplateView):
    """View da tela inicial"""
    template_name = "index.html"

    def get(self, request):
        return render(request, self.template_name, {'data': {
            'categoria': Categoria.objects.all(), 
            'status': StatusSenha.objects.all(),
            'tipo': Tipo.objects.all(),
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
            campus = Campus.objects.get(id=dados_form['campus'])
            if dados_form['status'] == 'on':
                status = True
            else:
                status = False
            guiche = Guiche(num_guiche= dados_form['num_guiche'],status=status, campus=campus)
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

class AtendimentoView(TemplateView):
    """Criando view para Tipo"""
    template_name = "atendimento.html"
    guiche = 1
    now = timezone.now

    def get(self, request):
        senhas = Senha.objects.all().order_by('hora_data')[0]
        senha, status =  str(senhas).split(',')

        print(senha, status)
        return render(request, self.template_name, {'senha': senha, 'status': status})


    def post(self, request):
        senha_obj = Senha.objects.filter(status='Na fila').order_by('-hora_data')[0]
        senha, status = str(senha_obj).split(',')
        senha_obj = Senha.objects.filter(senha=senha)
        senha_obj.status = StatusSenha.objects.get(nome='Em atendimento')
        senha_obj.save()
        atendimento = Atendimento()

        response = None
        return response