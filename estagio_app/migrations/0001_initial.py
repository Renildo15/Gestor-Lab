# Generated by Django 4.0.4 on 2022-07-05 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Estagio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estagiario', models.CharField(max_length=50)),
                ('orientador', models.CharField(max_length=50)),
                ('supervisor', models.CharField(max_length=50)),
                ('atividade', models.CharField(max_length=50)),
            ],
        ),
    ]
