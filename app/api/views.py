from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import TemplateView
from api.forms import CategoriaForm, StatusForm, TipoForm

class CategoriaView(TemplateView):
    template_name = "registrar_categoria.html"
    form_class = CategoriaForm

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/sucess/')

        return render(request, self.template_name, {'form':form})


class StatusView(TemplateView):
    template_name = "registrar_status.html"

class TipoView(TemplateView):
    template_name = "registar_tipo.html"