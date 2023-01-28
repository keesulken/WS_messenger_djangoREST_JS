from rest_framework import serializers
from .models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id',
                  'username',
                  'author',)


class SingleAuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('id',
                  'user',
                  'username',
                  'picture',
                  'chatroom_set',)


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('id',
                  'username',
                  'picture',)


class SingleChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatRoom
        fields = ('id',
                  'name',
                  'description',)


class ChatRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatRoom
        fields = ('id',
                  'name',
                  'admin',
                  'description',
                  'last_activity',
                  'user_list',)


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ('id',
                  'author',
                  'content',
                  'added',)
