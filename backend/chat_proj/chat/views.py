from django.views.generic import CreateView
from rest_framework import generics, viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from django.contrib.auth import get_user_model

from .serializers import *
from .forms import *

User = get_user_model()


class RegisterView(CreateView):
    model = User
    form_class = BaseRegisterForm
    success_url = '/'


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ChatRoomViewSet(viewsets.ModelViewSet):
    queryset = ChatRoom.objects.all()
    serializer_class = ChatRoomSerializer


class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer


class ChatDetailAPIView(APIView):
    def get(self, request, **kwargs):
        authenticated_user = request.user
        chat = ChatRoom.objects.get(pk=kwargs['pk'])
        admin = User.objects.get(pk=chat.admin_id)
        user_list = chat.user_list.all()
        msg_list = Message.objects.filter(chat=chat)
        current_user = AuthorizedUserSerializer(authenticated_user).data
        chat_data = SingleChatSerializer(chat).data
        admin_data = UserSerializer(admin).data
        msg_list_data = MessageSerializer(msg_list, many=True).data
        user_list_data = UserSerializer(user_list, many=True).data
        return Response({'current': current_user,
                         'chat': chat_data,
                         'admin': admin_data,
                         'users': user_list_data,
                         'messages': msg_list_data})


class ProfileAPIView(APIView):
    def get(self, request, **kwargs):
        user = request.user
        profile_data = UserSerializer(user).data
        if len(user.chatroom_set.all()) == 0:
            return Response({'user': profile_data,
                             'chat': 'null'})
        elif len(user.chatroom_set.all()) == 1:
            chat = user.chatroom_set.all().first()
            chat_data = ChatRoomSerializer(chat).data
            return Response({'user': profile_data,
                             'chat': chat_data})
        else:
            raw_chat_list = user.chatroom_set.all()
            chat_list = ChatRoomSerializer(raw_chat_list, many=True).data
            return Response({'user': profile_data,
                             'chat_list': chat_list})


class MessageAPIView(APIView):
    def post(self, request, **kwargs):
        msg = Message()
        msg.author = request.data['author']
        msg.content = request.data['text']
        msg.chat = request.data['chat']
        msg.save()
        return Response(status=status.HTTP_201_CREATED)


class UserChatAPIView(APIView):
    def get(self, request, **kwargs):
        user = User.objects.get(id=kwargs['user_id'])
        chats = []
        for i in ChatRoom.objects.all():
            if user in i.user_list.all():
                chats.append(i)
        chat_list = ChatRoomSerializer(chats, many=True).data
        return Response({'chats': chat_list})


class NewChatAPIView(APIView):
    def post(self, request, **kwargs):
        chat = ChatRoom()
        admin = User.objects.get(username=request.data['admin'])
        chat.name = request.data['name']
        chat.description = request.data['desc']
        chat.admin_id = admin.id
        chat.save()
        chat.user_list.add(admin)
        return Response({'id': chat.pk}, status=status.HTTP_201_CREATED)

