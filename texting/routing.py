from texting.consumers import PersonalChatConsumer
from django.urls import path

websocket_urlpatterns = [
    path('ws/<int:id>/', PersonalChatConsumer.as_asgi()), ]
