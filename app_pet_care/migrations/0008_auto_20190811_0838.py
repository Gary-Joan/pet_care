# Generated by Django 2.2.4 on 2019-08-11 14:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_pet_care', '0007_auto_20190811_0810'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='start_time',
            new_name='Fecha_y_Hora_Cita',
        ),
        migrations.RenameField(
            model_name='event',
            old_name='title',
            new_name='Mascota',
        ),
        migrations.RenameField(
            model_name='event',
            old_name='description',
            new_name='Problema',
        ),
    ]