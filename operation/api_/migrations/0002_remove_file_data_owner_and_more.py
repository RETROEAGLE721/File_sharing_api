# Generated by Django 4.2.7 on 2023-12-03 14:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api_', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='file_data',
            name='owner',
        ),
        migrations.RemoveField(
            model_name='users',
            name='no_files_uploaded',
        ),
        migrations.RemoveField(
            model_name='users',
            name='registration_date',
        ),
    ]