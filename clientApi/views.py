from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from rest_framework.response import Response
from rest_framework.views import APIView

from mysite.models import MyProfile
from .models import Message

from rest_framework import status
from clientApi.models import Message, Dialog, CurrentUser, EmptyDialog
from django.contrib.auth.models import User
from clientApi.serializers import MessagesSerializer, DialogsSerializer, ProfileSerializer, EmptyDialogsSerializer, CurrentUserSerializer, AddPastTravelSerializer
from mysite.models import AddPastTravel

from django.db.models import Q
import pycountry

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
        # получить определенный диалог
        elif (request.GET.get('dialog_id')):
            dialog = Dialog.objects.filter(dialog_id = request.GET.get('dialog_id'))
            dialogs_serializer = DialogsSerializer(dialog[0])
            
            if dialog[0].first_user_id == request.user:
                dialog_id = dialog[0].dialog_id
                interlocutor = dialog[0].second_user_id
                interlocutor_id = dialog[0].second_user_id.id
                interlocutor_fio = dialog[0].second_user_fio()
            else:
                dialog_id = dialog[0].dialog_id
                interlocutor = dialog[0].first_user_id
                interlocutor_id = dialog[0].first_user_id.id
                interlocutor_fio = dialog[0].first_user_fio()

            dialog = {
                'dialog_id': dialog_id,
                'interlocutor_fio': interlocutor_fio,
                'interlocutor_id': interlocutor_id,
                'is_online': MyProfile.objects.get(user=interlocutor).is_online,
                'last_online_at': MyProfile.objects.get(user=interlocutor).last_online_at
            }

            return JsonResponse(dialog, safe=False)
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
    
    def get_latest_message(self, latest_message):
        if latest_message is not None:
            return {
                'message_content': latest_message.message_content,
                'date': latest_message.sent_date,
                'author': latest_message.author_id.id
            }
        else:
            return None

    def user_dialogs(self, request):
        user = self.request.user
        realDialogs = Dialog.objects.filter(Q(first_user_id=user) | Q(second_user_id=user))
        emptyDialogs = EmptyDialog.objects.filter(Q(author_id=user))

        response_data = []

        for realDialog in realDialogs:
            # получаем информацию о собеседнике пользователя
            # last_message = Message.objects.filter(dialog_id=realDialog.dialog_id).latest('sent_date')
            messages = Message.objects.filter(dialog_id=realDialog.dialog_id).order_by('-sent_date')
            latest_message = messages.first()

            if realDialog.first_user_id == user:
                interlocutor = realDialog.second_user_fio()
                interlocutor_id = realDialog.second_user_id.id
                is_online = MyProfile.objects.get(user=realDialog.second_user_id).is_online
                if MyProfile.objects.get(user=realDialog.second_user_id).profile_image:
                    avatar = MyProfile.objects.get(user=realDialog.second_user_id).profile_image.url
                else:
                    avatar = ''

            else:
                interlocutor = realDialog.first_user_fio()
                interlocutor_id = realDialog.first_user_id.id
                is_online = MyProfile.objects.get(user=realDialog.first_user_id).is_online
                if MyProfile.objects.get(user=realDialog.first_user_id).profile_image:
                    avatar = MyProfile.objects.get(user=realDialog.first_user_id).profile_image.url
                else:
                    avatar = ''
             # добавляем информацию о диалоге в список
            response_data.append({
                'dialog_id': realDialog.dialog_id,
                'interlocutor': interlocutor,
                'interlocutor_id': interlocutor_id,
                'is_online': is_online,
                'last_message': self.get_latest_message(latest_message),
                'avatar': avatar,
            })

        for emptyDialog in emptyDialogs:
            # добавляем информацию о диалоге в список
            response_data.append({
                'dialog_id': emptyDialog.dialog_id,
                'interlocutor': emptyDialog.interlocutor(),
                'interlocutor_id': emptyDialog.interlocutor_id.id,
                'is_online': MyProfile.objects.get(user=emptyDialog.interlocutor_id).is_online,
                'avatar': MyProfile.objects.get(user=emptyDialog.interlocutor_id).profile_image if MyProfile.objects.get(user=emptyDialog.interlocutor_id).profile_image else '',
                'isEmptyDialog': True
            })

        return response_data
        


class CurrentUserView(APIView):
    def get(self, request):
        print('CurrentUserView', request.user)
        user_serializer = CurrentUserSerializer(request.user)
        return JsonResponse(user_serializer.data, safe=False)

class UserStatusView(APIView):
    def post(self, request):
        user_id = request.data.get('user_id')
        is_online = request.data.get('is_online')

        print('UserStatusView')
        if user_id and is_online is not None:
            print('UserStatusView if', user_id, is_online)
            user = User.objects.get(id=user_id)
            profile = MyProfile.objects.get(user=user)
            profile.is_online = is_online
            profile.save()

            return Response({'status': 'ok'})

        return Response({'status': 'error'})

class UserPopupInfoView(APIView):
    def get(self, request):
        user_id = request.GET.get('user_id')
        print('UserPopupInfoView', user_id)
        data = AddPastTravel.objects.filter(user_id=user_id).latest('when_traveled')
        serializer = AddPastTravelSerializer(data)
        
        # Получить объект страны по коду
        country = pycountry.countries.get(alpha_2=serializer.data['from_where'])

        travel_objects = AddPastTravel.objects.filter(user_id=user_id)
        unique_countries = set(obj.to_where for obj in travel_objects)

        user = User.objects.get(id=user_id)

        # ПОПРАВИТЬ
        unique_cities = set(obj.to_where for obj in travel_objects)
        countries_count = len(unique_countries)
        cities_count = len(unique_cities)

        return_data = {
            'user_name': user.first_name,
            'user_surname': user.last_name,
            'user_email': user.email,
            'from': country.name,
            'transport': serializer.data['transport_type'],
            'people': serializer.data['with_whom'],
            'cities_count': cities_count,
            'countries_count': countries_count,
        }
        return Response(return_data)

