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
                  'picture',)

    def create(self, validated_data):
        return Author.objects.create(**validated_data)


class ChatRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatRoom
        fields = ('name',
                  'admin_id',
                  'description',
                  'last_activity',
                  'user_list',)

    def create(self, validated_data):
        return ChatRoom.objects.create(**validated_data)


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ('author_id',
                  'chat_id',
                  'content',
                  'pinned',)

    def create(self, validated_data):
        return Message.objects.create(**validated_data)
