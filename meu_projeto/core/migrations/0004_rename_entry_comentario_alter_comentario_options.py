# Generated by Django 5.1.7 on 2025-04-01 19:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_rename_materias_materia_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Entry',
            new_name='Comentario',
        ),
        migrations.AlterModelOptions(
            name='comentario',
            options={'verbose_name_plural': 'comentarios'},
        ),
    ]
