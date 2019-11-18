from rest_framework import serializers
from .models import Senha

class SenhaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Senha
        fields = ['senha', 'hora_data']

