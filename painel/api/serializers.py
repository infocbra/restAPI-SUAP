from rest_framework import serializers
from django.utils import timezone
from api.models import Tipo, Senha, Categoria, Atendimento, StatusSenha


class TipoSerializer(serializers.ModelSerializer):
    """Serializer para os objetos Tipo"""
    class Meta:
        model = Tipo
        fields = ('id','nome',)
        read_only_fields = ('id',)


class SenhaSerializer(serializers.ModelSerializer):
    """Serializer para os objetos Senha"""
    class Meta:
        model = Senha
        fields = ('id', 'senha', 'tipo', 'categoria', 
                  'status', 'hora_data',)
        read_only_fields = ('id', 'senha', 'status',)
    
    def create(self, validated_data):
        """Create a new user with encripted password and return it"""
        senha = Senha(tipo = validated_data['tipo'], categoria= validated_data['categoria'], status= StatusSenha.objects.get(nome='Na fila'), senha= nova_senha(validated_data))
        senha.save()
        return senha


class CategoriaSerializer(serializers.ModelSerializer):
    """Serializer para os objetos Categoria"""
    class Meta:
        model = Categoria
        fields = ('id', 'nome',)
        read_only_fields = ('id',)


def nova_senha (validated_data):
    if Senha.objects.all():
        last_num = Senha.objects.all().order_by('-id')[0].senha
        nova_senha = validated_data['tipo'].nome[0] + validated_data['categoria'].nome[0] + '0' + str(int(last_num[2:]) + 1)
    else:
        nova_senha = validated_data['tipo'].nome[0] + validated_data['categoria'].nome[0] + "01"

    return nova_senha