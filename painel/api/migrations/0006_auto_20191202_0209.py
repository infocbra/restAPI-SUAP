# Generated by Django 2.2.4 on 2019-12-02 02:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20191202_0204'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guiche',
            name='status',
            field=models.BooleanField(default=True, verbose_name='ativo'),
        ),
    ]
