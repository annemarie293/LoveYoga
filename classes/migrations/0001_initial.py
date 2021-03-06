# Generated by Django 3.2 on 2022-01-12 23:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('trainers', '0003_rename_trainers_trainer'),
    ]

    operations = [
        migrations.CreateModel(
            name='YogaClass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('description', models.TextField()),
                ('practice', models.CharField(max_length=250)),
                ('level', models.CharField(max_length=250)),
                ('intensity', models.CharField(max_length=250)),
                ('session_duration', models.IntegerField()),
                ('series_duration', models.IntegerField()),
                ('equipment', models.CharField(blank=True, max_length=250, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('trainer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='trainers.trainer')),
            ],
            options={
                'verbose_name_plural': 'YogaClasses',
            },
        ),
    ]
