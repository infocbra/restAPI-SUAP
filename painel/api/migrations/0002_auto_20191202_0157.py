# Generated by Django 2.2.4 on 2019-12-02 01:57

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='senha',
            name='hora_data',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 12, 2, 1, 57, 29, 985747, tzinfo=utc)),
        ),
    ]
