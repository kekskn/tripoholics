from rest_framework import serializers
from clientApi.models import Messages, Users

class MessagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Messages
        fields = ('MessageId', 'MessageContent', 'MessageName')

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ('UserId', 'UserName', 'Message', 'DateOfRegistration', 'PhotoFileName')
