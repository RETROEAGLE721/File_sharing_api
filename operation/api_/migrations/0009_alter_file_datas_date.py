# Generated by Django 4.2.7 on 2023-12-11 05:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_', '0008_file_datas'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file_datas',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 11, 11, 25, 0, 613720)),
        ),
    ]
