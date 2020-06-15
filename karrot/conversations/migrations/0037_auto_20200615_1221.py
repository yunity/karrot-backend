# Generated by Django 3.0.2 on 2020-06-15 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conversations', '0036_add_conversation_meta'),
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
