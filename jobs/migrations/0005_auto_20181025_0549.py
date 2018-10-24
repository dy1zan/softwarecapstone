# Generated by Django 2.0.6 on 2018-10-24 16:49

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0004_auto_20181025_0309'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 24, 16, 49, 23, 404355, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='job',
            name='expiry',
            field=models.DateTimeField(default=datetime.datetime(2018, 11, 7, 16, 49, 23, 404355, tzinfo=utc)),
        ),
    ]