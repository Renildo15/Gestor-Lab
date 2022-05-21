# Generated by Django 4.0.4 on 2022-05-20 21:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('membros_app', '0003_alter_membro_laboratorio_alter_membro_membro_perfil'),
        ('laboratorio_app', '0003_alter_lab_coordenador_alter_lab_vice_coordenador'),
    ]

    operations = [
        migrations.CreateModel(
            name='Artigo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50)),
                ('local_Publi', models.CharField(max_length=150)),
                ('descricao', models.CharField(max_length=150)),
                ('autores', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='autores', to='membros_app.membro')),
                ('laboratorio_art', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='laboratorio_art', to='laboratorio_app.lab')),
            ],
        ),
    ]