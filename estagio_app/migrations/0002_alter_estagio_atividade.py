# Generated by Django 4.0.4 on 2022-07-08 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estagio_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estagio',
            name='atividade',
            field=models.CharField(max_length=200),
        ),
    ]
