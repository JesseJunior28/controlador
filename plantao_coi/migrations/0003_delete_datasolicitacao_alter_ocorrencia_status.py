# Generated by Django 5.1.5 on 2025-05-12 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plantao_coi', '0002_alter_comentario_options_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='DataSolicitacao',
        ),
        migrations.AlterField(
            model_name='ocorrencia',
            name='status',
            field=models.CharField(choices=[('EM_ABERTO', 'Em Aberto'), ('CONCLUIDA', 'Concluida'), ('CANCELADA', 'Cancelada')], default='EM_ABERTO', max_length=10, verbose_name='Status'),
        ),
    ]
