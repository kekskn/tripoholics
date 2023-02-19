from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()
# Create your models here.

class Messages(models.Model):
    author = models.ForeignKey(User, related_name='author_messages', on_delete=models.CASCADE)
    MessageId = models.AutoField(primary_key=True)
    MessageContent = models.CharField(max_length=500)
    MessageName = models.CharField(max_length=50)

class Users(models.Model):
    UserId = models.AutoField(primary_key=True)
    UserName = models.CharField(max_length=500)
    Message = models.CharField(max_length=50)
    DateOfRegistration = models.DateField()
    PhotoFileName = models.CharField(max_length=500)

