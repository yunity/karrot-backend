# Generated by Django 3.1.2 on 2020-11-08 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webhooks', '0005_auto_20190918_1219'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emailevent',
            name='payload',
            field=models.JSONField(),
        ),
        migrations.AlterField(
            model_name='incomingemail',
            name='payload',
            field=models.JSONField(),
        ),
    ]
