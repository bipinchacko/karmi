# Generated by Django 3.2 on 2021-04-25 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0006_message_delete'),
    ]

    operations = [
        migrations.AddField(
            model_name='groupmessage',
            name='files',
            field=models.FileField(blank=True, null=True, upload_to='chat'),
        ),
    ]
