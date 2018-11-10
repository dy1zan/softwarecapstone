# Generated by Django 2.0.6 on 2018-11-03 07:37

import apps.user.models.user
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_user_verify_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='verify_code',
            field=models.IntegerField(default=apps.user.models.user.generate_random_code),
        ),
    ]