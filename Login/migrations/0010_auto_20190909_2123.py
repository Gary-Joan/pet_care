# Generated by Django 2.2.4 on 2019-09-10 03:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Login', '0009_auto_20190821_0810'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grademedic',
            name='grade_doctor',
            field=models.CharField(choices=[('N', '-------'), ('b', 'Regular'), ('g', 'Bueno'), ('e', 'Excelente')], default='N', max_length=1),
        ),
    ]
