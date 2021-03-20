# Generated by Django 3.1.7 on 2021-03-09 10:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('longprofile', '0005_auto_20210309_0610'),
    ]

    operations = [
        migrations.CreateModel(
            name='Connection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('connection', models.ImageField(default=0, upload_to='')),
                ('connected_time', models.DateTimeField(auto_now=True)),
                ('connected_person', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='who_connected', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='who_requested', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
