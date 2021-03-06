# Generated by Django 3.1.7 on 2021-03-23 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('longprofile', '0018_auto_20210322_2054'),
    ]

    operations = [
        migrations.RenameField(
            model_name='personal_card',
            old_name='logo',
            new_name='back_img',
        ),
        migrations.RenameField(
            model_name='personal_card',
            old_name='photo',
            new_name='front_img',
        ),
        migrations.RemoveField(
            model_name='personal_card',
            name='address1',
        ),
        migrations.RemoveField(
            model_name='personal_card',
            name='address2',
        ),
        migrations.RemoveField(
            model_name='personal_card',
            name='address3',
        ),
        migrations.RemoveField(
            model_name='personal_card',
            name='job',
        ),
        migrations.RemoveField(
            model_name='personal_card',
            name='phone1',
        ),
        migrations.RemoveField(
            model_name='personal_card',
            name='phone2',
        ),
        migrations.AddField(
            model_name='personal_card',
            name='company_location',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='personal_card',
            name='details',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='personal_card',
            name='location',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='personal_card',
            name='mobile',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='personal_card',
            name='services',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='personal_card',
            name='website',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='personal_card',
            name='whatsup',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='personal_card',
            name='company_name',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='personal_card',
            name='email',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='personal_card',
            name='name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
