# rest_framework
from rest_framework import viewsets, mixins
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

# serializers
from api import serializers

# models 
from api.models import Categoria, StatusSenha, Senha, Tipo


class SenhaViewSet(viewsets.GenericViewSet, 
                     mixins.ListModelMixin,
                     mixins.CreateModelMixin):
    """Gerenciando as senhas no banco de dados"""
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Senha.objects.all()
    serializer_class = serializers.SenhaSerializer

    def perform_create(self, serializer):
        """Register a new patient"""
        serializer.save()


class CategoriaViewSet(viewsets.GenericViewSet, 
                     mixins.ListModelMixin,
                     mixins.CreateModelMixin):
    """Gerenciando as senhas no banco de dados"""
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Categoria.objects.all()
    serializer_class = serializers.CategoriaSerializer


class TipoViewSet(viewsets.GenericViewSet, 
                     mixins.ListModelMixin,
                     mixins.CreateModelMixin):
    """Gerenciando as senhas no banco de dados"""
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Tipo.objects.all()
    serializer_class = serializers.TipoSerializer
