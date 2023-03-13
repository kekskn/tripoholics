from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Message

from clientApi.models import Message, Dialog, CurrentUser
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

    def post(self, request):
        message = request.data
        # Create a message from the above data
        serializer = MessagesSerializer(data=message)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return JsonResponse({"success": True})


class DialogView(APIView):
    def get(self, request):
        if (request.GET.get('user_id')):
            dialogs = Dialog.objects.filter(Q(first_user_id = request.GET.get('user_id')) | Q(second_user_id = request.GET.get('user_id')))
            dialogs_serializer = DialogsSerializer(dialogs, many=True)
            return JsonResponse(dialogs_serializer.data, safe=False)
        elif (request.GET.get('dialog_id')):
            dialog = Dialog.objects.filter(dialog_id = request.GET.get('dialog_id'))
            dialogs_serializer = DialogsSerializer(dialog[0])
            return JsonResponse(dialogs_serializer.data, safe=False)
        else:
            response_data = self.user_dialogs(request)
            return Response(response_data)
        
    def user_dialogs(self, request):
        user = self.request.user
        dialogs = Dialog.objects.filter(Q(first_user_id=user) | Q(second_user_id=user))

        response_data = []

        for dialog in dialogs:
            # получаем информацию о собеседнике пользователя
            if dialog.first_user_id == user:
                interlocutor = dialog.second_user_fio()
            else:
                interlocutor = dialog.first_user_fio()

             # добавляем информацию о диалоге в список
            response_data.append({
                'dialog_id': dialog.dialog_id,
                'interlocutor': interlocutor,
            })

        return response_data
        


class CurrentUserView(APIView):
    def get(self, request):
        user_serializer = CurrentUserSerializer(request.user)
        # user_serializer = CurrentUserSerializer(request.user.currentuser)
        return JsonResponse(user_serializer.data, safe=False)
        # current_user = CurrentUser.objects.get(user=request.user)
        # user_serializer = CurrentUserSerializer(current_user)
        # return JsonResponse(user_serializer.data, safe=False)


        # current_user = request.user.currentuser
        # serializer = CurrentUserSerializer(current_user)
        # return Response(serializer.data)