# Generated by Django 3.1.7 on 2021-03-06 09:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(max_length=254, null=True, unique=True, verbose_name='email address')),
                ('username', models.CharField(max_length=150, null=True, unique=True)),
                ('first_name', models.CharField(blank=True, max_length=150)),
                ('last_name', models.CharField(blank=True, max_length=150)),
                ('start_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UserExtend',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=100, null=True)),
                ('created_by', models.CharField(max_length=100, null=True)),
                ('position', models.CharField(max_length=100, null=True)),
                ('profession', models.CharField(max_length=100, null=True)),
                ('institution_name', models.CharField(max_length=100, null=True)),
                ('degree', models.CharField(max_length=100, null=True)),
                ('specilisation', models.CharField(max_length=100, null=True)),
                ('start_year', models.CharField(max_length=100, null=True)),
                ('end_year', models.CharField(max_length=100, null=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Follow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('follow_time', models.DateTimeField(auto_now=True)),
                ('follower', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='who_following', to=settings.AUTH_USER_MODEL)),
                ('following', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='who_follows', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
