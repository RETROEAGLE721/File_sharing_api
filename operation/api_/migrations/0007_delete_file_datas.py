# Generated by Django 4.2.7 on 2023-12-04 06:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api_', '0006_remove_file_datas_unique_id_alter_file_datas_name'),
    ]

    operations = [
        migrations.DeleteModel(
            name='file_datas',
        ),
    ]
