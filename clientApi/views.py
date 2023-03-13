from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Message

from rest_framework import status
from clientApi.models import Message, Dialog, CurrentUser, EmptyDialog
from django.contrib.auth.models import User
from clientApi.serializers import MessagesSerializer, DialogsSerializer, CurrentUserSerializer, EmptyDialogsSerializer

from django.db.models import Q

# Create your views here.

# @csrf_exempt
# def messagesApi(request, id=0):
#     if request.method == 'GET':
#         messages = Message.objects.all()
#         messages_serializer = MessagesSerializer(messages, many=True)
#         return JsonResponse(messages_serializer.data, safe=False)
#     elif request.method == 'POST':
#         messages_data=JSONParser().parse(request)
#         messages_serializer = MessagesSerializer(data=messages_data)
#         if messages_serializer.is_valid():
#             messages_serializer.save()
#             return JsonResponse("Message added successfully", safe=False)
#         return JsonResponse("Failed to add message", safe=False)


class MessageView(APIView):
    def get(self, request):
        messages = Message.objects.filter(dialog_id = request.GET.get('dialogId'))
        messages_serializer = MessagesSerializer(messages, many=True)
        return JsonResponse(messages_serializer.data, safe=False)

    def post(self, request):
        author_id = request.data.get('author_id')
        dialog_id = request.data.get('dialog_id')
        message_content = request.data.get('message_content')
        is_new_dialog = request.data.get('is_new_dialog')

        if is_new_dialog:
            recipient_id = request.data.get('interlocutor_id')
            # Создаем новый диалог или находим существующий
            newDialog = DialogView().create_dialog(request, author_id, recipient_id)
            print('after creating new dialog')
            EmptyDialog.objects.filter(dialog_id=dialog_id).delete()
            print('after deleting empty dialog')
            # Добавляем автора и получателя в список участников
            # dialog.members.add(author_id, recipient_id)
            # Создаем новое сообщение в диалоге
            message_data = {
                'author_id': author_id,
                'dialog_id': newDialog.dialog_id,
                'message_content': message_content,
            }

            message_serializer = MessagesSerializer(data=message_data)

            if message_serializer.is_valid():
                print('first ser is valid')
                author_id = message_serializer.validated_data.get('author_id')
                dialog_id = message_serializer.validated_data.get('dialog_id')
                message_content = message_serializer.validated_data.get('message_content')
                print('create first')
                # Message.objects.create(author_id=author_id, dialog_id=dialog_id, message_content=message_content)
                message = Message.objects.create(dialog_id=newDialog, author_id=author_id, message_content=message_content)
                # Отправляем ответ с информацией о новом диалоге и сообщении
                return Response({'success': True, 'new_dialog_id': newDialog.dialog_id, 'first_message': message.message_id })

        message_data = {
            'author_id': author_id,
            'dialog_id': dialog_id,
            'message_content': message_content,
        }

        message_serializer = MessagesSerializer(data=message_data)

        if message_serializer.is_valid():
            author_id = message_serializer.validated_data.get('author_id')
            dialog_id = message_serializer.validated_data.get('dialog_id')
            message_content = message_serializer.validated_data.get('message_content')
            print('create firsecond')

            Message.objects.create(author_id=author_id, dialog_id=dialog_id, message_content=message_content)
            return JsonResponse({"success": True})


class DialogView(APIView):
    def create_dialog(self, request, author_id, recipient_id):
        # Проверяем, есть ли уже диалог между автором и получателем
        dialog = Dialog.objects.filter(first_user_id=author_id, second_user_id=recipient_id).first()
        if not dialog:
            dialog = Dialog.objects.filter(first_user_id=recipient_id, second_user_id=author_id).first()
        # Если диалога нет, создаем его
        if not dialog:
            first_user = User.objects.get(id=author_id)
            second_user = User.objects.get(id=recipient_id)
            dialog = Dialog.objects.create(first_user_id=first_user, second_user_id=second_user)
        return dialog

    def get(self, request):
        if (request.GET.get('user_id')):
            dialogs = Dialog.objects.filter(Q(first_user_id = request.GET.get('user_id')) | Q(second_user_id = request.GET.get('user_id')))
            dialogs_serializer = DialogsSerializer(dialogs, many=True)
            return JsonResponse(dialogs_serializer.data, safe=False)
        elif (request.GET.get('dialog_id')):
            dialog = Dialog.objects.filter(dialog_id = request.GET.get('dialog_id'))
            dialogs_serializer = DialogsSerializer(dialog[0])
            return JsonResponse(dialogs_serializer.data, safe=False)
        elif (request.GET.get('emptyDialog_id')):
            emptyDialog = EmptyDialog.objects.filter(dialog_id = request.GET.get('emptyDialog_id'))
            empty_dialogs_serializer = EmptyDialogsSerializer(emptyDialog[0])
            return JsonResponse(empty_dialogs_serializer.data, safe=False)
        else:
            response_data = self.user_dialogs(request)
            return Response(response_data)
    
    def post(self, request):
        print('dataa: ', request.data)
        serializer = EmptyDialogsSerializer(data=request.data)
        if serializer.is_valid():
            print('serializer is valid')
            author_id = serializer.validated_data.get('author_id')
            interlocutor_id = serializer.validated_data.get('interlocutor_id')

            print('dataaaaq: ', author_id, interlocutor_id)
            # Проверяем, существует ли уже пустой диалог между автором и собеседником
            realDialog = Dialog.objects.filter(
                Q(first_user_id = author_id) & Q(second_user_id = interlocutor_id) | 
                Q(first_user_id = interlocutor_id) & Q(second_user_id = author_id)
            )
            emptyDialog = EmptyDialog.objects.filter(
                author_id=author_id,
                interlocutor_id=interlocutor_id
            )
            if realDialog.exists():
                print('realDialog.exists')

                return Response({'error': 'Real dialog already exists', 'dialogId': realDialog.first().dialog_id}, status=status.HTTP_400_BAD_REQUEST)

            if emptyDialog.exists():
                print('emptyDialog.exists')

                # Если пустой диалог уже существует, возвращаем его данные в ответе
                # data = self.serializer_class(dialogs.first()).data
                return Response({'error': 'Empty dialog already exists', 'dialogId': emptyDialog.first().dialog_id}, status=status.HTTP_400_BAD_REQUEST)
            else:
                # Создаем новый пустой диалог
                dialog = EmptyDialog.objects.create(
                    author_id=author_id,
                    interlocutor_id=interlocutor_id
                )
                return Response({'success': True, 'dialogId': dialog.dialog_id})

    def user_dialogs(self, request):
        user = self.request.user
        realDialogs = Dialog.objects.filter(Q(first_user_id=user) | Q(second_user_id=user))
        emptyDialogs = EmptyDialog.objects.filter(Q(author_id=user))

        response_data = []

        for realDialog in realDialogs:
            # получаем информацию о собеседнике пользователя
            if realDialog.first_user_id == user:
                interlocutor = realDialog.second_user_fio()
            else:
                interlocutor = realDialog.first_user_fio()

             # добавляем информацию о диалоге в список
            response_data.append({
                'dialog_id': realDialog.dialog_id,
                'interlocutor': interlocutor,
            })

        for emptyDialog in emptyDialogs:
            # получаем информацию о собеседнике пользователя
            # if realDialog.first_user_id == user:
            #     interlocutor = realDialog.second_user_fio()
            # else:
            #     interlocutor = realDialog.first_user_fio()

             # добавляем информацию о диалоге в список
            response_data.append({
                'dialog_id': emptyDialog.dialog_id,
                'interlocutor': emptyDialog.interlocutor(),
                'isEmptyDialog': True
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