# Generated by Django 4.0.5 on 2022-06-08 18:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('horario_app', '0003_alter_horario_horario'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='horario',
            name='dia',
        ),
        migrations.RemoveField(
            model_name='horario',
            name='horario',
        ),
        migrations.RemoveField(
            model_name='horario',
            name='turno',
        ),
    ]