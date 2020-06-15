# Generated by Django 3.0.2 on 2020-06-15 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conversations', '0037_set_non-nullable_values'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conversationmeta',
            name='conversations_marked_at',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='conversationmeta',
            name='threads_marked_at',
            field=models.DateTimeField(),
        ),
    ]
