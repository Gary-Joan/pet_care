# Generated by Django 2.2.4 on 2019-08-11 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_pet_care', '0005_auto_20190810_1536'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
            ],
        ),
    ]
