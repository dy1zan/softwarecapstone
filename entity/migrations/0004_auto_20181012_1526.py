# Generated by Django 2.0.6 on 2018-10-12 02:26

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entity', '0003_group'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='name',
            field=models.CharField(max_length=80, validators=[django.core.validators.RegexValidator(message='Your name can only include characters 0-9, A-Z or a-z.', regex='^[0-9A-Za-z]$')]),
        ),
    ]
