# Generated by Django 3.2.13 on 2022-07-01 22:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evento_app', '0006_alter_evento_site'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evento',
            name='descricao',
            field=models.TextField(max_length=200),
        ),
    ]