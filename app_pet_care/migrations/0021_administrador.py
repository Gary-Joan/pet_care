# Generated by Django 2.2.6 on 2019-10-18 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_pet_care', '0020_delete_grademedic'),
    ]

    operations = [
        migrations.CreateModel(
            name='Administrador',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('dpi', models.IntegerField()),
                ('telephone', models.CharField(max_length=10)),
                ('mail', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
            ],
        ),
    ]