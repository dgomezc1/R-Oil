# Generated by Django 3.2.6 on 2021-09-06 02:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('estudiante', '0002_alter_estudiante_barrio'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='estudiante',
            options={'verbose_name': 'Estudiante', 'verbose_name_plural': 'Estudiantes'},
        ),
    ]