# chat/routing.py
from django.urls import re_path

from . import consumers

websocket_urlpatterns = [
    # re_path(r"ws/chat/(?P<room_name>\w+)/$", consumers.ChatConsumer.as_asgi()),
    re_path(r"ws/my_messages/(?P<room_name>\w+)/$", consumers.ChatConsumer.as_asgi()),
    re_path(r'ws/online_status/(?P<user_id>\d+)/$', consumers.OnlineStatusConsumer.as_asgi()),
]