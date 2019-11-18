from django.urls import path, re_path, include
from rest_framework.routers import DefaultRouter
from api import views

router = DefaultRouter()
router.register('all', views.SenhaViewSet)
router.register('categoria', views.CategoriaViewSet)
router.register('tipo', views.TipoViewSet)

app_name = 'api'


urlpatterns = [
    path('', include(router.urls)),
]