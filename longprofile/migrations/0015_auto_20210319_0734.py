# Generated by Django 3.1.7 on 2021-03-19 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('longprofile', '0014_auto_20210319_0729'),
    ]

    operations = [
        migrations.AlterField(
            model_name='createappoinment',
            name='date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='createappoinment',
            name='time',
            field=models.TimeField(),
        ),
    ]
