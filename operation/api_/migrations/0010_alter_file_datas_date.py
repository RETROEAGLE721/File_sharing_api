# Generated by Django 4.2.7 on 2023-12-23 05:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_', '0009_alter_file_datas_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file_datas',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 23, 11, 17, 51, 51513)),
        ),
    ]