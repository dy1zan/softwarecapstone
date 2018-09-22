# Generated by Django 2.0.6 on 2018-09-22 05:01

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0007_auto_20180908_1440'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companyapplication',
            name='date_submitted',
            field=models.DateField(default=datetime.date(2018, 9, 22)),
        ),
        migrations.AlterField(
            model_name='companymembers',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='members', to=settings.AUTH_USER_MODEL),
        ),
    ]
