# Generated by Django 3.2 on 2022-01-10 23:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trainers', '0002_rename_description_trainers_bio'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Trainers',
            new_name='Trainer',
        ),
    ]
