# Generated by Django 4.1.5 on 2023-01-25 22:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0004_chatroom_private'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='chat_list',
        ),
    ]