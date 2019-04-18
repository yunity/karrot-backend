# Generated by Django 2.1.5 on 2019-01-13 16:27
import django
from django.db import migrations

import karrot


class Migration(migrations.Migration):

    dependencies = [
        ('pickups', '0011_pickupdate_migrate_to_date_range'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pickupdate',
            options={},
        ),
        migrations.RemoveField(
            model_name='pickupdate',
            name='date',
        ),
        migrations.AlterModelOptions(
            name='pickupdate',
            options={'ordering': ['date_range']},
        ),
        migrations.AlterModelOptions(
            name='pickupdate',
            options={'ordering': ['date']},
        ),
        migrations.RenameField(
            model_name='pickupdate',
            old_name='date_range',
            new_name='date',
        ),
        migrations.AlterField(
            model_name='pickupdate',
            name='date',
            field=django.contrib.postgres.fields.ranges.DateTimeRangeField(default=karrot.pickups.models.default_pickup_date_range),
        ),
    ]