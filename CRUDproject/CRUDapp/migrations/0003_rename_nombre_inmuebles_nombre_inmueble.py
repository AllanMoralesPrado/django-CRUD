# Generated by Django 3.2.5 on 2022-04-07 17:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CRUDapp', '0002_inmuebles_m2_terreno'),
    ]

    operations = [
        migrations.RenameField(
            model_name='inmuebles',
            old_name='nombre',
            new_name='nombre_inmueble',
        ),
    ]
