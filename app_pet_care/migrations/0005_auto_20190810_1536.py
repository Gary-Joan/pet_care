# Generated by Django 2.2.4 on 2019-08-10 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_pet_care', '0004_auto_20190810_1531'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pet_appointment',
            name='pet_name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
