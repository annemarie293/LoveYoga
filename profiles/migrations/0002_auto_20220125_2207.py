# Generated by Django 3.2 on 2022-01-25 22:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='default_email',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='default_full_name',
        ),
    ]
