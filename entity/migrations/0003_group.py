# Generated by Django 2.0.6 on 2018-10-10 10:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('entity', '0002_auto_20181010_1612'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('entity_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='entity.Entity')),
                ('name', models.CharField(max_length=80)),
                ('description', models.CharField(max_length=500)),
                ('website', models.CharField(max_length=100)),
            ],
            bases=('entity.entity',),
        ),
    ]
