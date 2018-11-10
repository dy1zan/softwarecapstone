# Generated by Django 2.0.6 on 2018-10-24 08:53

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entity', '0002_auto_20181016_0423'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='address',
            field=models.CharField(default=None, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='contact_email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='company',
            name='contact_phone',
            field=models.CharField(max_length=15, validators=[django.core.validators.RegexValidator(message='A phone number can only contain numbers.', regex='^[0-9]*$')]),
        ),
        migrations.AlterField(
            model_name='company',
            name='specialist_area',
            field=models.CharField(max_length=1530),
        ),
        migrations.AlterField(
            model_name='company',
            name='website',
            field=models.URLField(max_length=300),
        ),
    ]