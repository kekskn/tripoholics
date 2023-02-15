from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from clientApi.models import Messages, Users
from clientApi.serializers import MessagesSerializer, UsersSerializer


# Create your views here.

@csrf_exempt
def messagesApi(request, id=0):
    if request.method == 'GET':
        messages = Messages.objects.all()
        messages_serializer = MessagesSerializer(messages, many=True)
        return JsonResponse(messages_serializer.data, safe=False)
    elif request.method == 'POST':
        messages_data=JSONParser().parse(request)
        messages_serializer = MessagesSerializer(data=messages_data)
        if messages_serializer.is_valid():
            messages_serializer.save()
            return JsonResponse("Message added successfully", safe=False)
        return JsonResponse("Failed to add message", safe=False)