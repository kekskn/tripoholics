from rest_framework import serializers
from django.contrib.auth.models import User
from clientApi.models import Message, Dialog, CurrentUser


class DialogsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dialog
        fields = ('test', 'dialog_id', 'first_user_id', 'second_user_id')

class MessagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ('author_id', 'message_id', 'dialog_id', 'message_content')

class CurrentUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name')
