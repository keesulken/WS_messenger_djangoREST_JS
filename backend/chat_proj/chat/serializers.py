from rest_framework import serializers

from .models import *


class AuthorizedUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id',
                  'username',
                  'picture',)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id',
                  'username',
                  'picture',)


class SingleChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatRoom
        fields = ('id',
                  'admin_id',
                  'name',
                  'description',)


class ChatRoomSerializer(serializers.ModelSerializer):
    last_activity = serializers.DateTimeField(format="%d-%b-%y %H:%M")

    class Meta:
        model = ChatRoom
        fields = ('id',
                  'name',
                  'admin_id',
                  'description',
                  'private',
                  'last_activity',
                  'user_list',)


class MessageSerializer(serializers.ModelSerializer):
    added = serializers.DateTimeField(format="%d-%b-%y %H:%M")

    class Meta:
        model = Message
        fields = ('id',
                  'author',
                  'content',
                  'chat',
                  'added',)
