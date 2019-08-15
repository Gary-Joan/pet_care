# Generated by Django 2.2.4 on 2019-08-13 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EventCita',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doctor', models.CharField(max_length=25)),
                ('pet_owner', models.CharField(max_length=25)),
                ('title', models.CharField(max_length=200)),
                ('race', models.CharField(max_length=25)),
                ('description', models.TextField()),
                ('symptons', models.TextField()),
                ('prescription', models.TextField()),
                ('start_time', models.DateField()),
                ('end_time', models.DateField()),
                ('date_start_time', models.TimeField()),
                ('date_end_time', models.TimeField()),
            ],
        ),
    ]
