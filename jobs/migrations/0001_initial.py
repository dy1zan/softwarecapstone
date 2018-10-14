# Generated by Django 2.0.6 on 2018-10-14 06:51

import datetime
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('entity', '0006_auto_20181012_1532'),
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('description', models.TextField(max_length=2550.0)),
                ('contact_email', models.EmailField(max_length=254)),
                ('contact_phone', models.CharField(max_length=15, validators=[django.core.validators.RegexValidator(message='A phone number can only contain numbers.', regex='^[0-9]*$')])),
                ('expiry', models.DateTimeField(default=datetime.datetime(2018, 10, 28, 6, 51, 43, 477858, tzinfo=utc))),
                ('external_link', models.CharField(max_length=2083)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='jobs', to='entity.Company')),
            ],
        ),
    ]
