from django.db import models
from django.contrib.auth.models import User


class Author(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=64)
    picture = models.FileField(upload_to=None)


class ChatRoom(models.Model):
    name = models.CharField(max_length=128)
    admin = models.OneToOneField(Author, on_delete=models.DO_NOTHING)
    user_list = models.ManyToManyField(Author, through='UserChat')
    description = models.CharField(max_length=255)
    last_activity = models.DateTimeField(auto_now=True)


class Message(models.Model):
    author = models.ForeignKey(Author, on_delete=models.DO_NOTHING)
    chat = models.ForeignKey(ChatRoom, on_delete=models.CASCADE)
    content = models.TextField()
    pinned = models.FileField(upload_to=None)


class UserChat(models.Model):
    user = models.ForeignKey(Author, on_delete=models.CASCADE)
    chat = models.ForeignKey(ChatRoom, on_delete=models.CASCADE)

