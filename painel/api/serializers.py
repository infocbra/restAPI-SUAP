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
        fields = ('id', 'senha', 'fk_tipo', 'fk_categoria', 
                  'fk_status', 'hora_data',)
        read_only_fields = ('id', 'senha','hora_data', 'fk_status',)
    
    def create(self, validated_data):
        """Create a new user with encripted password and return it"""
        if Senha.objects.all():
            last_num = Senha.objects.all().order_by('-id')[0].senha
            nova_senha = validated_data['fk_tipo'].nome[0] + validated_data['fk_categoria'].nome[0] + str(int(last_num[2:]) + 1)
            senha = Senha(fk_tipo = validated_data['fk_tipo'], fk_categoria= validated_data['fk_categoria'], fk_status= StatusSenha.objects.get(nome='Na fila'), senha= nova_senha)
        else:
            nova_senha = validated_data['fk_tipo'].nome[0] + validated_data['fk_categoria'].nome[0] + "01"
            tipo = validated_data['fk_tipo']
            cat = validated_data['fk_categoria']
            senha = Senha(fk_tipo = validated_data['fk_tipo'], fk_categoria= validated_data['fk_categoria'], fk_status= StatusSenha.objects.get(nome='Na fila'), senha= nova_senha)
            
        senha.save()
        return senha


class CategoriaSerializer(serializers.ModelSerializer):
    """Serializer para os objetos Categoria"""
    class Meta:
        model = Categoria
        fields = ('id', 'nome',)
        read_only_fields = ('id',)


        
# class TipoSerializer(serializers.ModelSerializer):
#     id_tipo = serializers.IntegerField(primary_key=True, null=False)
#     nome = serializers.CharField(max_length=80, null=False)

#     def get_tipo(self):
#         atendimento = Atendimento.objects.all()
#         for i in atendimento:
#             print(i) # Depois colocar um redirect para uma página html.

# class SenhaSerializer(serializers.ModelSerializer):
#     id_senha = serializers.IntegerField(primary_key=True, null=False)
#     senha = serializers.IntegerField(null=False)
#     hora_data = serializers.DateTimeField(default=datetime.now(), blank=True)

#     def post_senha(self):
#         senha = Senha().save() #Ainda não sei o que colocar dentro de senha

# class CategoriaSerializer(serializers.ModelSerializer):
#     id_categoria = serializers.IntegerField(primary_key=True, null=False)
#     nome = serializers.CharField(max_length=80, null=False)

# class AtendimentoSerializer(serializers.ModelSerializer):
#     id_atendimento = serializers.IntegerField(primary_key=True, null=False)
#     hora_data_ini = serializers.DateTimeField()
#     hora_data_fim = serializers.DateTimeField()


