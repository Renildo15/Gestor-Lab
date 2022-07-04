# Generated by Django 4.0.4 on 2022-05-18 23:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('laboratorio_app', '0003_alter_lab_coordenador_alter_lab_vice_coordenador'),
        ('evento_app', '0002_evento_data_sbm'),
    ]

    operations = [
        migrations.AddField(
            model_name='evento',
            name='laboratorio',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='laboratorio_app.lab'),
        ),
    ]