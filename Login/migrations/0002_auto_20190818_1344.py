# Generated by Django 2.2.4 on 2019-08-18 19:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Login', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='clientprofile',
            old_name='direction',
            new_name='address',
        ),
    ]
