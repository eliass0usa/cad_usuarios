# Generated by Django 5.0.7 on 2024-07-30 15:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_cad_usuarios', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Usuarios',
            new_name='Usuario',
        ),
    ]