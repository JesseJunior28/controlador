# Generated by Django 5.1.5 on 2025-04-07 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plantao_coi', '0006_rename_dataencerramento_datasolicitacao_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ocorrencia',
            name='descricao',
            field=models.TextField(blank=True, null=True, verbose_name='Descrição da Ocorrência'),
        ),
    ]
