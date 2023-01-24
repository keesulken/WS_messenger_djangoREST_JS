from django.db import models
from django.contrib.auth.models import User


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=64)
    picture = models.ImageField(upload_to='profile_pics/', blank=True)
    chat_list = models.ManyToManyField('ChatRoom', through='UserChat')

    def __str__(self):
        return f'Author {self.username}'


class ChatRoom(models.Model):
    name = models.CharField(max_length=128)
    admin = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    user_list = models.ManyToManyField(Author, through='UserChat')
    description = models.CharField(max_length=255, blank=True)
    last_activity = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name}'


class Message(models.Model):
    author = models.ForeignKey(Author, on_delete=models.DO_NOTHING)
    chat = models.ForeignKey(ChatRoom, on_delete=models.CASCADE)
    content = models.TextField()
    added = models.DateTimeField(auto_now_add=True)
    pinned = models.ImageField(upload_to='pinned_pics/', blank=True)

    def __str__(self):
        return f'Msg {self.content[:20]}'


class UserChat(models.Model):
    user = models.ForeignKey(Author, on_delete=models.CASCADE)
    chat = models.ForeignKey(ChatRoom, on_delete=models.CASCADE)
