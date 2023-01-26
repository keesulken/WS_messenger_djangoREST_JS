from django.views.generic import CreateView
from rest_framework import generics, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import *
from .forms import *


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class ChatRoomViewSet(viewsets.ModelViewSet):
    queryset = ChatRoom.objects.all()
    serializer_class = ChatRoomSerializer


class ChatDetail(APIView):
    def get(self, request, **kwargs):
        chat = ChatRoom.objects.get(pk=kwargs['pk'])
        msg_list = Message.objects.filter(chat=chat).values()
        return Response({'messages': list(msg_list)})


class RegisterView(CreateView):
    model = User
    form_class = BaseRegisterForm
    success_url = '/'


class ProfileAPIView(APIView):

    # def get(self, request, **kwargs):
    #     author = request.user.author
    #     print(author.chat_list)
    #     return Response({'username': author.username,
    #                     'picture': author.get_picture_url})

    def get(self, request, **kwargs):
        author = request.user.author
        profile_data = AuthorSerializer(instance=author).data
        if len(author.chatroom_set.all()) == 0:
            return Response({'user': profile_data,
                             'chat': 'null'})
        elif len(author.chatroom_set.all()) == 1:
            chat = author.chatroom_set.all().first()
            chat_data = ChatRoomSerializer(instance=chat).data
            return Response({'user': profile_data,
                             'chat': chat_data})
        else:
            chat_list = list(author.chatroom_set.all().values())
            return Response({'user': profile_data,
                             'chat_list': chat_list})
