# Generated by Django 2.2.4 on 2019-08-11 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_pet_care', '0006_event'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pet_appointment',
            name='pet_name',
            field=models.CharField(max_length=200),
        ),
    ]
