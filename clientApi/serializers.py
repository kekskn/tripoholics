from rest_framework import serializers
from django.contrib.auth.models import User
from clientApi.models import Message, Dialog, CurrentUser


class DialogsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dialog
        fields = ('dialog_id', 'first_user_id', 'second_user_id', 'first_user_fio', 'second_user_fio')

class MessagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ('author_id', 'message_id', 'dialog_id', 'message_content', 'sent_date')
    
        def create(self, validated_data):
            return Message.objects.create(**validated_data)



# class CurrentUserSerializer(serializers.ModelSerializer):
#     # is_online = CurrentUserProfileSerializer()
#     street = serializers.CharField(max_length=500)

#     class Meta:
#         model = User
#         fields = ('id', 'first_name', 'last_name', 'street')
#         # fields = ('__all__')
#         # model = CurrentUser
#         # fields = ('is_online')

# class CurrentUserProfileSerializer(serializers.ModelSerializer):
#     currentUser = CurrentUserSerializer()
#     class Meta:
#         model = CurrentUser
#         fields = ('street', 'currentUser')
#         depth=1

class CurrentUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name')

# class CurrentUserSerializer(serializers.ModelSerializer):
#     user = UserSerializer(source='currentuser')
#     street = serializers.CharField(max_length=500)

#     class Meta:
#         model = CurrentUser
#         fields = ('id', 'user', 'street')