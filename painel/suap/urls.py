from django.urls import path
from suap import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('registrar', views.RegistrarView.as_view(), name='registrar'),
    path('atendimento', views.AtendimentoView.as_view(), name='atendimento'),
]

# Adicionando caminhos para CRUD Categorias
urlpatterns += [
    path('categoria/adicionar', views.CategoriaCreate.as_view(), name='adicionar_categoria'),
    path('categoria/<int:pk>/atualizar/', views.CategoriaUpdate.as_view(), name='atualizar_categoria'),
    path('categoria/<int:pk>/deletar/', views.CategoriaDelete.as_view(), name='deletar_categoria'),    
]

# Adicionando caminhos para CRUD Status
urlpatterns += [
    path('status/adicionar', views.StatusCreate.as_view(), name='adicionar_status'),
    path('status/<int:pk>/atualizar/', views.StatusUpdate.as_view(), name='atualizar_status'),
    path('status/<int:pk>/deletar/', views.StatusDelete.as_view(), name='deletar_status'),    
]

# Adicionando caminhos para CRUD Tipo
urlpatterns += [
    path('tipo/adicionar', views.TipoCreate.as_view(), name='adicionar_tipo'),
    path('tipo/<int:pk>/atualizar/', views.TipoUpdate.as_view(), name='atualizar_tipo'),
    path('tipo/<int:pk>/deletar/', views.TipoDelete.as_view(), name='deletar_tipo'),    
]

# Adicionando caminhos para CRUD Campus
urlpatterns += [
    path('campus/adicionar', views.CampusCreate.as_view(), name='adicionar_campus'),
    path('campus/<int:pk>/atualizar/', views.CampusUpdate.as_view(), name='atualizar_campus'),
    path('campus/<int:pk>/deletar/', views.CampusDelete.as_view(), name='deletar_campus'),    
]

# Adicionando caminhos para CRUD Guiche
urlpatterns += [
    path('guiche/adicionar', views.GuicheCreate.as_view(), name='adicionar_guiche'),
    path('guiche/<int:pk>/atualizar/', views.GuicheUpdate.as_view(), name='atualizar_guiche'),
    path('guiche/<int:pk>/deletar/', views.GuicheDelete.as_view(), name='deletar_guiche'),    
]

# Adicionando caminhos para CRUD Atendente
urlpatterns += [
    path('atendente/adicionar', views.AtendenteCreate.as_view(), name='registrar_atendente'),
    path('atendente/<int:pk>/atualizar/', views.AtendenteUpdate.as_view(), name='atualizar_atendente'),
    path('atendente/<int:pk>/deletar/', views.AtendenteDelete.as_view(), name='deletar_atendente'),    
]


# Adicionando caminhas para Chamar nova Senha, Chamar senha novamente
urlpatterns += [
    path('senha/chamar/nova', views.ChamarNovaSenhaView.as_view(), name='chamar_nova_senha'),
    path('senha/chamar/<int:pk>/', views.ChamarSenhaNovamenteView.as_view(), name='chamar_senha_novamente')
]