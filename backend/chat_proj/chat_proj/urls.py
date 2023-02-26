"""chat_proj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView

from chat.views import *
from chat_proj import settings
from rest_framework import routers

user_router = routers.SimpleRouter()
user_router.register(r'user', UserViewSet)

chat_router = routers.SimpleRouter()
chat_router.register(r'chat', ChatRoomViewSet)

msg_router = routers.SimpleRouter()
msg_router.register(r'msg', MessageViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/profile/', ProfileAPIView.as_view()),
    path('account/profile/', TemplateView.as_view(template_name='prof.html')),
    path('account/chat/<int:pk>', TemplateView.as_view(template_name='chat.html')),
    path('account/ws/1', TemplateView.as_view(template_name='ws.html')),

    path('api/v1/chatroom/<int:pk>', ChatDetailAPIView.as_view()),
    path('api/v1/user_chats/<int:user_id>', UserChatAPIView.as_view()),
    path('api/v1/chatroom/new_msg/<int:chat_id>', NewMessageAPIView.as_view()),
    path('api/v1/chatroom/new/', NewChatAPIView.as_view()),
    path('api/v1/chatroom/new_private/', NewPrivateChatAPIView.as_view()),
    path('api/v1/chatroom/new_user/<int:chat_id>', AddNewUserToChatAPIView.as_view()),
    path('api/v1/profile_picture/<int:user_id>', AddUserPictureAPIView.as_view()),
    path('api/v1/profile_name/<int:user_id>', UserChangeNameAPIView.as_view()),


    path('register/', RegisterView.as_view(template_name='signup.html')),
    path('login/', RegisterView.as_view(template_name='login.html')),
    path('logout/', TemplateView.as_view(template_name='logout.html')),


    path('api/v1/', include(user_router.urls)),
    path('api/v1/', include(chat_router.urls)),
    path('api/v1/', include(msg_router.urls)),


    path('api/v1/auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
