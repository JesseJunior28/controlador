# Generated by Django 5.1.5 on 2025-04-03 23:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plantao_coi', '0005_alter_ocorrencia_status'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='DataEncerramento',
            new_name='DataSolicitacao',
        ),
        migrations.DeleteModel(
            name='DataAbertura',
        ),
        migrations.RemoveField(
            model_name='ocorrencia',
            name='data_abertura',
        ),
        migrations.RemoveField(
            model_name='ocorrencia',
            name='data_encerramento',
        ),
        migrations.AddField(
            model_name='ocorrencia',
            name='data_solicitacao',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Data da Solicitação'),
        ),
    ]
