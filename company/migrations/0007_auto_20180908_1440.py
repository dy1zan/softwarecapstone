# Generated by Django 2.0.6 on 2018-09-08 02:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0006_auto_20180908_1418'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companyapplication',
            name='date_submitted',
            field=models.DateField(default=datetime.date(2018, 9, 8)),
        ),
    ]