from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import TemplateView
from api.forms import CategoriaForm, StatusForm, TipoForm
from api.models import Categoria, StatusSenha, Tipo



class IndexView(TemplateView):
    template_name = "index.html"

    def get(self, request):
        return render(request, self.template_name, {'data': {
            'categoria': Categoria.objects.all(), 
            'status': StatusSenha.objects.all(),
            'tipo': Tipo.objects.all()
            }})


class CategoriaView(TemplateView):
    template_name = "registrar_categoria.html"
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
    template_name = "registrar_status.html"
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
    template_name = "registar_tipo.html"
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