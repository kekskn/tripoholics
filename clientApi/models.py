from django.contrib.auth.models import User
from django.contrib import admin
from django.db import models
import uuid

# User = get_user_model()
# Create your models here.

class Dialog(models.Model):
    test = models.CharField(max_length=20)
    dialog_id = models.AutoField(primary_key=True)
    first_user_id = models.ForeignKey(User, related_name='first_user', on_delete=models.CASCADE)
    second_user_id = models.ForeignKey(User, related_name='second_user', on_delete=models.CASCADE)

    def __str__(self):
        return f'Author 1: {self.first_user_id.username}, Author 2: {self.second_user_id.username}'

class Message(models.Model):
    message_id = models.AutoField(primary_key=True)
    author_id = models.ForeignKey(User, related_name='author_messages', on_delete=models.CASCADE)
    dialog_id = models.ForeignKey(Dialog, on_delete=models.CASCADE)
    message_content = models.CharField(max_length=500)

    def __str__(self):
        return f'{self.message_content}'


class CurrentUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
