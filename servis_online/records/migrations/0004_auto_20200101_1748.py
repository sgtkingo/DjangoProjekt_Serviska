# Generated by Django 3.0.1 on 2020-01-01 16:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0003_auto_20200101_1727'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 1, 17, 48, 36, 188501)),
        ),
    ]
