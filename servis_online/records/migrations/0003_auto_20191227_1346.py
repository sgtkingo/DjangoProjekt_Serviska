# Generated by Django 3.0.1 on 2019-12-27 12:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0002_auto_20191227_1332'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 27, 13, 46, 52, 111169)),
        ),
    ]