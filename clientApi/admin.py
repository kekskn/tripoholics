from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin
from .models import Message, Dialog, CurrentUser

# Register your models here.

admin.site.register(Message)
admin.site.register(Dialog)
admin.site.register(CurrentUser)
