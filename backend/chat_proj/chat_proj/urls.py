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
from django.urls import path, include
from django.views.generic import TemplateView

from chat.views import *
from chat_proj import settings
from rest_framework import routers

user_router = routers.SimpleRouter()
user_router.register(r'user', UserViewSet)

author_router = routers.SimpleRouter()
author_router.register(r'author', AuthorViewSet)

chat_router = routers.SimpleRouter()
chat_router.register(r'chat', ChatRoomViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('rest_framework.urls')),
    path('api/v1/profile/', ProfileAPIView.as_view()),
    path('account/profile/', TemplateView.as_view(template_name='profile.html')),
    path('api/v1/', include(user_router.urls)),
    path('api/v1/', include(author_router.urls)),
    path('api/v1/', include(chat_router.urls)),
    path('api/v1/chatroom/<int:pk>', ChatDetail.as_view()),
    path('register/', RegisterView.as_view(template_name='signup.html')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
