# Generated by Django 2.2.4 on 2019-12-02 01:59

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20191202_0158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='senha',
            name='hora_data',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
        ),
    ]
