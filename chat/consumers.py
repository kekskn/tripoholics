# chat/consumers.py
import json
from django.contrib.auth import get_user_model

from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer

from django.utils import timezone

timezone.localtime(timezone.now())

User = get_user_model()

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        # print('================')
        # print(User)
        # print('================')
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = "chat_%s" % self.room_name

        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name, self.channel_name
        )

        self.accept()

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name, self.channel_name
        )

    # Receive message from WebSocket
    def receive(self, text_data):
        print('receiveee: ', text_data)
        text_data_json = json.loads(text_data)
        message_content = text_data_json["message_content"]
        author_id = text_data_json["author_id"]
        print(author_id)
        

        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name, {"type": "chat_message", "message_content": message_content, "author_id": author_id}
        )

    # Receive message from room group
    def chat_message(self, event):
        print('EVENTT: ', event)
        message_content = event["message_content"]
        author_id = event["author_id"]


        # Send message to WebSocket
        self.send(text_data=json.dumps({"message_content": message_content, "author_id": author_id, "sent_date": timezone.now().isoformat()}))