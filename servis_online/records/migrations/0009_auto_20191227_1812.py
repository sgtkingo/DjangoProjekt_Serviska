# Generated by Django 3.0.1 on 2019-12-27 17:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0008_auto_20191227_1755'),
    ]

    operations = [
        migrations.AddField(
            model_name='solution',
            name='solution_type',
            field=models.CharField(choices=[('HW_REP', 'Hardware Repair'), ('HW_CHG', 'Hardware Change'), ('SW_RES', 'Software Reinstall'), ('SW_REP', 'Software Repair'), ('OTHER', 'Other repair')], default='NON', max_length=6),
        ),
        migrations.AlterField(
            model_name='record',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 27, 18, 12, 23, 216320)),
        ),
    ]