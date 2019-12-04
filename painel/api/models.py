from django.db import models
from django.utils import timezone
from django.utils.translation import gettext as _
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, \
                                        PermissionsMixin

class UserManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):
        """ Creates and save a new user"""
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        """Creates and save a new superuser"""
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """Custom user model that supports email nstead off username"""
    email = models.EmailField(max_length=255, null=False, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    
    objects = UserManager()

    USERNAME_FIELD = 'email'


class StatusSenha(models.Model):
    nome = models.CharField(max_length=80, null=False, default='Na fila')

    def __str__(self):
        return self.nome


class Tipo(models.Model):
    nome = models.CharField(max_length=80, null=False)

    def __str__(self):
        return self.nome


class Categoria(models.Model):
    nome = models.CharField(max_length=80, null=False)

    def __str__(self):
        return self.nome


class Senha(models.Model):
    tipo = models.ForeignKey(Tipo, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    status = models.ForeignKey(StatusSenha, on_delete=models.CASCADE)
    senha = models.CharField(max_length = 255, null=False)
    hora_data = models.DateTimeField(default=timezone.now, blank=True)

    def __str__(self):
        return self.senha, self.hora_data


class Campus(models.Model):
    campus = models.CharField(max_length=30, null=False)

    def __str__(self):
        return self.campus


class Atendente(models.Model):
    Siape = models.IntegerField()
    Nome = models.CharField(max_length=30, null=False)

    def __str__(self):
        return self.Siape


class Guiche(models.Model):
    num_guiche = models.CharField(max_length=10, null=False)
    status = models.BooleanField(verbose_name=_('Em atendimento'), default=False)
    campus = models.ForeignKey(Campus, on_delete=models.CASCADE)

    def __str__(self):
        return self.num_guiche


class Atendimento(models.Model):
    hora_data_ini = models.DateTimeField()#linha modificada por DanielB
    hora_data_fim = models.DateTimeField() # Acrescentar horário para termino
    atendente = models.ForeignKey(Atendente, on_delete=models.CASCADE)
    guiche = models.ForeignKey(Guiche, on_delete=models.CASCADE)
    senha = models.ForeignKey(Senha, on_delete=models.CASCADE)

    def __str__(self):
        return self.hora_data_ini
