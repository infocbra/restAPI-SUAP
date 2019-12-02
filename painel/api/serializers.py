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
        read_only_fields = ('id', 'senha','hora_data', 'status',)
    
    def create(self, validated_data):
        """Create a new user with encripted password and return it"""
        if Senha.objects.all():
            last_num = Senha.objects.all().order_by('-id')[0].senha
            nova_senha = validated_data['tipo'].nome[0] + validated_data['categoria'].nome[0] + str(int(last_num[2:]) + 1)
        else:
            nova_senha = validated_data['tipo'].nome[0] + validated_data['categoria'].nome[0] + "01"
        tipo = validated_data['tipo']
        cat = validated_data['categoria']
        senha = Senha(tipo = validated_data['tipo'], categoria= validated_data['categoria'], status= StatusSenha.objects.get(nome='Na fila'), senha= nova_senha)
            
        senha.save()
        return senha


class CategoriaSerializer(serializers.ModelSerializer):
    """Serializer para os objetos Categoria"""
    class Meta:
        model = Categoria
        fields = ('id', 'nome',)
        read_only_fields = ('id',)


