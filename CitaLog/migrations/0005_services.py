# Generated by Django 2.2.4 on 2019-10-17 04:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CitaLog', '0004_auto_20190815_1409'),
    ]

    operations = [
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_name', models.CharField(max_length=25)),
                ('description', models.CharField(max_length=25)),
                ('doctor_who_doit', models.CharField(max_length=200)),
            ],
        ),
    ]