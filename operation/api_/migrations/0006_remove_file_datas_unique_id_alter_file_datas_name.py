# Generated by Django 4.2.7 on 2023-12-04 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_', '0005_alter_file_datas_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='file_datas',
            name='unique_id',
        ),
        migrations.AlterField(
            model_name='file_datas',
            name='name',
            field=models.FileField(upload_to=''),
        ),
    ]
