# Generated by Django 3.2.6 on 2021-10-28 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('premios', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='premio',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='premios/pictures'),
        ),
    ]
