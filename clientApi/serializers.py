from rest_framework import serializers
from django.contrib.auth.models import User
from clientApi.models import Message, Dialog, CurrentUser, EmptyDialog


class DialogsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dialog
        fields = ('dialog_id', 'first_user_id', 'second_user_id', 'first_user_fio', 'second_user_fio')

class EmptyDialogsSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmptyDialog
        fields = ('dialog_id', 'author', 'interlocutor', 'interlocutor_id', 'author_id')

class MessagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ('author_id', 'message_id', 'dialog_id', 'message_content', 'sent_date')
    
        def create(self, validated_data):
            return Message.objects.create(**validated_data)

class CurrentUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name')
