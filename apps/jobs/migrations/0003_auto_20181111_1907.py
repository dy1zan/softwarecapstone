# Generated by Django 2.0.6 on 2018-11-11 06:07

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0002_auto_20181103_2037'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2018, 11, 11, 6, 7, 52, 317586, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='job',
            name='expiry',
            field=models.DateTimeField(default=datetime.datetime(2018, 11, 25, 6, 7, 52, 317586, tzinfo=utc)),
        ),
    ]
