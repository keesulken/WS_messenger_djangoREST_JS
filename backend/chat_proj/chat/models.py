from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    picture = models.ImageField(upload_to='profile_pics/', blank=True)
    token = models.CharField(max_length=255, blank=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['picture', 'token']

    @property
    def get_picture_url(self):
        if self.picture and hasattr(self.picture, 'url'):
            return self.picture.url
        else:
            return 'media/profile_pics/default.png'


class ChatRoom(models.Model):
    name = models.CharField(max_length=128)
    admin_id = models.IntegerField()
    user_list = models.ManyToManyField(User, through='UserChat')
    description = models.CharField(max_length=255, blank=True)
    private = models.BooleanField(default=False)
    last_activity = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name}'


class Message(models.Model):
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    chat = models.ForeignKey(ChatRoom, on_delete=models.CASCADE)
    content = models.TextField()
    added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Msg {self.content[:20]}'


class UserChat(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    chat = models.ForeignKey(ChatRoom, on_delete=models.CASCADE)
