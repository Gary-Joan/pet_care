# Generated by Django 2.2.4 on 2019-08-21 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Login', '0005_auto_20190821_0749'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grademedic',
            name='grade_doctor',
            field=models.CharField(choices=[('b', 'Regular'), ('g', 'Bueno'), ('e', 'Excelente')], default='b', max_length=1),
        ),
    ]
