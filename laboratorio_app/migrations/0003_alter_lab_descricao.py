# Generated by Django 4.0.4 on 2022-07-04 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('laboratorio_app', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lab',
            name='descricao',
            field=models.TextField(max_length=200),
        ),
    ]
