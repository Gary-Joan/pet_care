# Generated by Django 2.2.4 on 2019-08-10 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_pet_care', '0003_delete_event'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pet_appointment',
            name='hour',
            field=models.TimeField(),
        ),
    ]
