from django.db import models
from datetime import datetime

class StatusSenha(models.Model):
    id_statusSenha = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=80, null=False)

class Tipo(models.Model):
    id_tipo = models.IntegerField(primary_key=True, null=False)
    nome = models.CharField(max_length=80, null=False)

class Categoria(models.Model):
    id_categoria = models.IntegerField(primary_key=True, null=False)
    nome = models.CharField(max_length=80, null=False)

class Senha(models.Model):
    id_senha = models.IntegerField(primary_key=True, null=False)
    fk_tipo = models.ForeignKey(Tipo, on_delete=models.CASCADE)
    fk_categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    fk_status = models.ForeignKey(StatusSenha, on_delete=models.CASCADE)
    senha = models.IntegerField(null=False)
    hora_data = models.DateTimeField(default=datetime.now(), blank=True)

class Campus(models.Model):
    id_campus = models.IntegerField(primary_key=True, null=False)
    Campo = models.CharField(max_length=30, null=False)

class Atendente(models.Model):
    id_atendente = models.IntegerField(primary_key=True, null=False)
    Siape = models.IntegerField()
    Nome = models.CharField(max_length=30, null=False)

class Guiche(models.Model):
    id_guiche = models.IntegerField(primary_key=True, null=False)
    nmr_guiche = models.CharField(max_length=10, null=False)
    status = models.BooleanField()
    fk_campus = models.ForeignKey(Campus, on_delete=models.CASCADE)

class Atendimento(models.Model):
    id_atendimento = models.IntegerField(primary_key=True, null=False)
    hora_data_ini = models.DateTimeField(default=datetime.now(), blank=True)
    hora_data_fim = models.DateTimeField() # Acrescentar horário para termino
    fk_atendente = models.ForeignKey(Atendente, on_delete=models.CASCADE)
    fk_guiche = models.ForeignKey(Guiche, on_delete=models.CASCADE)
    fk_senha = models.ForeignKey(Senha, on_delete=models.CASCADE)
