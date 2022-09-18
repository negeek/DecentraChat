from texting.consumers import PersonalChatConsumer, GroupChatConsumer
from django.urls import path

websocket_urlpatterns = [
    path('ws/<int:id>/', PersonalChatConsumer.as_asgi()),
    path('ws/group/<int:group_id>/', GroupChatConsumer.as_asgi()), ]
