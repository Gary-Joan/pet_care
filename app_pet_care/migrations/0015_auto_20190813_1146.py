# Generated by Django 2.2.4 on 2019-08-13 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_pet_care', '0014_auto_20190813_1145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='veterinarian',
            name='photo',
            field=models.FileField(blank=True, null=True, upload_to='media/imagen_veterinarian'),
        ),
    ]
