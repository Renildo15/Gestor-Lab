# Generated by Django 4.0.5 on 2022-06-10 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evento_app', '0003_evento_laboratorio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evento',
            name='descricao',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='evento',
            name='site',
            field=models.URLField(),
        ),
    ]