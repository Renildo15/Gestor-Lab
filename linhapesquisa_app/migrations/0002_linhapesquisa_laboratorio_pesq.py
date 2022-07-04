# Generated by Django 4.0.4 on 2022-05-21 11:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('laboratorio_app', '0003_alter_lab_coordenador_alter_lab_vice_coordenador'),
        ('linhapesquisa_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='linhapesquisa',
            name='laboratorio_pesq',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='laboratorio_pesq', to='laboratorio_app.lab'),
        ),
    ]