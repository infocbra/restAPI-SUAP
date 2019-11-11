from django.urls import path, re_path
from api import views


urlpatterns = [
    path('registrar/categoria', views.CategoriaView.as_view(), name='rgistrar_categoria'),
    path('registrar/tipo', views.TipoView.as_view(), name='registrar_tipo'),
    path('registrar/Status', views.StatusView.as_view(), name='registrar_status')
]