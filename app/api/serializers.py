from rest_framework import serializers
from .models import Senha, Categoria

class SenhaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Senha
        fields = ['senha', 'hora_data']

