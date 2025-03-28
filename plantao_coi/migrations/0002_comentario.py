# Generated by Django 5.1.5 on 2025-03-28 19:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plantao_coi', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto', models.TextField()),
                ('data_criacao', models.DateTimeField(auto_now_add=True)),
                ('ocorrencia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comentarios', to='plantao_coi.ocorrencia')),
            ],
        ),
    ]
