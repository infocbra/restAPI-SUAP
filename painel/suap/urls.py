from django.urls import path
from suap import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('registrar/categoria', views.CategoriaView.as_view(), name='registrar_categoria'),
    path('registrar/tipo', views.TipoView.as_view(), name='registrar_tipo'),
    path('registrar/status', views.StatusView.as_view(), name='registrar_status'),
    path('registrar/guiche', views.GuicheView.as_view(), name='registrar_guiche'),
    path('registrar/campus', views.CampusView.as_view(), name='registrar_campus'),
    path('registrar/atendente', views.AtendenteView.as_view(), name='registrar_atendente'),
]