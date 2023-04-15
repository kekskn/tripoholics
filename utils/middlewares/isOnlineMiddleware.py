from django.contrib.auth.models import User
from django.core.cache import cache
from django.utils import timezone
from django.utils.deprecation import MiddlewareMixin

from mysite.models import MyProfile
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

from django.contrib.auth.signals import user_logged_out

class ActiveUserMiddleware(MiddlewareMixin):

    def __init__(self, get_response=None):
        super().__init__(get_response)
        user_logged_out.connect(self.user_logged_out_callback)

    def user_logged_out_callback(self, sender, request, user, **kwargs):
        if user.is_authenticated:
            print('user_logged_out_callback', request.user)
            my_profile = MyProfile.objects.get(user=request.user)
            print('CURRENT USER LOGED OUT: ', my_profile.id, my_profile.is_online)
            my_profile.is_online = False
            my_profile.last_online_at = timezone.now()
            my_profile.save()
            self.set_user_offline(user, user.id)

    @staticmethod
    def set_user_online(user, user_id):
        print('set_user_online', user_id)
        channel_layer = get_channel_layer()
        group_name = f'online_status_{user_id}'
        last_online_at = MyProfile.objects.get(user=user).last_online_at
        print('set_user_online -- last_online_at', last_online_at)
        async_to_sync(channel_layer.group_send)(group_name, {
            'type': 'status_update', 
            'user_id': user_id, 
            'is_online': True,
            'last_online_at': str(last_online_at)
        })

    @staticmethod
    def set_user_offline(user, user_id):
        print('set_user_offline', user_id)
        channel_layer = get_channel_layer()
        group_name = f'online_status_{user_id}'
        last_online_at = MyProfile.objects.get(user=user).last_online_at
        print('set_user_offline -- last_online_at', last_online_at)
        async_to_sync(channel_layer.group_send)(group_name, {
            'type': 'status_update', 
            'user_id': user_id, 
            'is_online': False, 
            'last_online_at': str(last_online_at)
        })


    def process_request(self, request):
        print('process_request')
        if request.user.is_authenticated and request.session.session_key and '/update_is_online/' not in request.path:
            print('process_request if')
            cache_key = f'last-seen-{request.user.id}'
            last_login = cache.get(cache_key)
            print('last_login: ', last_login)

            if not last_login:
                User.objects.filter(id=request.user.id).update(last_login=timezone.now())
                # Устанавливаем кэширование на 300 секунд с текущей датой по ключу last-seen-id-пользователя
                cache.set(cache_key, timezone.now(), 300)
            try:
                my_profile = MyProfile.objects.get(user=request.user)
                if last_login is not None and timezone.now() < last_login + timezone.timedelta(seconds=300):
                    my_profile.is_online = True
                    my_profile.last_online_at = None
                    self.set_user_online(request.user, request.user.id) # Отправляем сообщение о статусе онлайн
                else:
                    my_profile.is_online = False
                    my_profile.last_online_at = timezone.now()
                    self.set_user_offline(request.user, request.user.id) # Отправляем сообщение о статусе онлайн
                my_profile.save()
            except MyProfile.DoesNotExist:
                pass