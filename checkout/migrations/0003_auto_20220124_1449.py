# Generated by Django 3.2 on 2022-01-24 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0002_auto_20220124_1102'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='classes_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='order',
            name='product_count',
            field=models.IntegerField(default=0),
        ),
    ]
