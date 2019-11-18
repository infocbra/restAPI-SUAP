from rest_framework import serializers
from datetime import datetime
from .models import Tipo, Senha, Categoria, Atendimento

class TipoSerializer(serializers.ModelSerializer):
    id_tipo = serializers.IntegerField(primary_key=True, null=False)
    nome = serializers.CharField(max_length=80, null=False)

    def get_tipo(self):
        atendimento = Atendimento.objects.all()
        for i in atendimento:
            print(i) # Depois colocar um redirect para uma página html.

class SenhaSerializer(serializers.ModelSerializer):
    id_senha = serializers.IntegerField(primary_key=True, null=False)
    senha = serializers.IntegerField(null=False)
    hora_data = serializers.DateTimeField(default=datetime.now(), blank=True)

    def post_senha(self):
        senha = Senha().save() #Ainda não sei o que colocar dentro de senha

class CategoriaSerializer(serializers.ModelSerializer):
    id_categoria = serializers.IntegerField(primary_key=True, null=False)
    nome = serializers.CharField(max_length=80, null=False)

class AtendimentoSerializer(serializers.ModelSerializer):
    id_atendimento = serializers.IntegerField(primary_key=True, null=False)
    hora_data_ini = serializers.DateTimeField()
    hora_data_fim = serializers.DateTimeField()


