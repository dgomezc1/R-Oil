# Generated by Django 3.2.5 on 2021-10-07 00:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0003_alter_user_options'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='docente',
            new_name='admin_docente',
        ),
        migrations.RemoveField(
            model_name='user',
            name='institucion',
        ),
        migrations.RemoveField(
            model_name='user',
            name='ni',
        ),
    ]
