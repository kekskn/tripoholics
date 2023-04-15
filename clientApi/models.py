from django.contrib.auth.models import User, AbstractUser
from django.contrib import admin
from django.db import models
from django.utils import timezone
from django.core.cache import cache

timezone.localtime(timezone.now())

class Dialog(models.Model):
    dialog_id = models.AutoField(primary_key=True)
    first_user_id = models.ForeignKey(User, related_name='first_user', on_delete=models.CASCADE)
    second_user_id = models.ForeignKey(User, related_name='second_user', on_delete=models.CASCADE)

    def first_user_fio(self):
        self.first_user_fio = f'{self.first_user_id.first_name} {self.first_user_id.last_name}'
        self.save()
        return self.first_user_fio

    def second_user_fio(self):
        self.second_user_fio = f'{self.second_user_id.first_name} {self.second_user_id.last_name}'
        self.save()
        return self.second_user_fio

    def __str__(self):
        return f'Author 1: {self.first_user_id.username}, Author 2: {self.second_user_id.username}'

class EmptyDialog(models.Model):
    dialog_id = models.AutoField(primary_key=True)
    author_id = models.ForeignKey(User, related_name='author', on_delete=models.CASCADE)
    interlocutor_id = models.ForeignKey(User, related_name='interlocutor', on_delete=models.CASCADE)
    
    def author(self):
        return f'{self.author_id.first_name} {self.author_id.last_name}'

    def interlocutor(self):
        return f'{self.interlocutor_id.first_name} {self.interlocutor_id.last_name}'

class Message(models.Model):
    message_id = models.AutoField(primary_key=True)
    author_id = models.ForeignKey(User, related_name='author_messages', on_delete=models.CASCADE)
    dialog_id = models.ForeignKey(Dialog, on_delete=models.CASCADE)
    message_content = models.CharField(max_length=500)
    sent_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.message_content}'


class CurrentUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
