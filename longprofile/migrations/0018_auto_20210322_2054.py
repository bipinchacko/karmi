# Generated by Django 3.1.7 on 2021-03-22 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('longprofile', '0017_createappoinment2_active'),
    ]

    operations = [
        migrations.RenameField(
            model_name='company_card',
            old_name='logo',
            new_name='back_img',
        ),
        migrations.RemoveField(
            model_name='company_card',
            name='address1',
        ),
        migrations.RemoveField(
            model_name='company_card',
            name='address2',
        ),
        migrations.RemoveField(
            model_name='company_card',
            name='address3',
        ),
        migrations.RemoveField(
            model_name='company_card',
            name='job',
        ),
        migrations.RemoveField(
            model_name='company_card',
            name='phone1',
        ),
        migrations.RemoveField(
            model_name='company_card',
            name='phone2',
        ),
        migrations.AddField(
            model_name='company_card',
            name='company_location',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='company_card',
            name='details',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='company_card',
            name='front_img',
            field=models.ImageField(blank=True, null=True, upload_to='media'),
        ),
        migrations.AddField(
            model_name='company_card',
            name='location',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='company_card',
            name='mobile',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='company_card',
            name='services',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='company_card',
            name='website',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='company_card',
            name='whatsup',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='company_card',
            name='company_name',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='company_card',
            name='email',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='company_card',
            name='name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
