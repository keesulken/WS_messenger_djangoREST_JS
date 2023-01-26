from rest_framework import serializers
from .models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id',
                  'username',
                  'author',)


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('user',
                  'username',
                  'picture',
                  'chatroom_set',)


class ChatRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatRoom
        fields = ('name',
                  'admin',
                  'description',
                  'last_activity',
                  'user_list',)


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ('author',
                  'chat',
                  'content',
                  'added',
                  'pinned',)
