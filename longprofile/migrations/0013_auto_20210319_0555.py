# Generated by Django 3.1.7 on 2021-03-19 05:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('longprofile', '0012_savedenquiry'),
    ]

    operations = [
        migrations.AlterField(
            model_name='savedenquiry',
            name='enquiry',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='longprofile.createenquiry'),
        ),
    ]
