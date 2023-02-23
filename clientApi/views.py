from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Message

from clientApi.models import Message, Dialog
from django.contrib.auth.models import User
from clientApi.serializers import MessagesSerializer, DialogsSerializer, CurrentUserSerializer

from django.db.models import Q

# Create your views here.

@csrf_exempt
def messagesApi(request, id=0):
    if request.method == 'GET':
        messages = Message.objects.all()
        messages_serializer = MessagesSerializer(messages, many=True)
        return JsonResponse(messages_serializer.data, safe=False)
    elif request.method == 'POST':
        messages_data=JSONParser().parse(request)
        messages_serializer = MessagesSerializer(data=messages_data)
        if messages_serializer.is_valid():
            messages_serializer.save()
            return JsonResponse("Message added successfully", safe=False)
        return JsonResponse("Failed to add message", safe=False)

class MessageView(APIView):
    def get(self, request):
        messages = Message.objects.filter(dialog_id = request.GET.get('dialogId'))
        messages_serializer = MessagesSerializer(messages, many=True)
        return JsonResponse(messages_serializer.data, safe=False)

class DialogView(APIView):
    def get(self, request):
        dialogs = Dialog.objects.filter(Q(first_user_id = request.GET.get('user_id')) | Q(second_user_id = request.GET.get('user_id')))
        dialogs_serializer = DialogsSerializer(dialogs, many=True)
        return JsonResponse(dialogs_serializer.data, safe=False)

class CurrentUserView(APIView):
    def get(self, request):
        user_serializer = CurrentUserSerializer(request.user)
        return JsonResponse(user_serializer.data, safe=False)