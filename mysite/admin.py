from django.contrib import admin
from .models import MyUser, MyProfile

admin.site.register(MyUser)
admin.site.register(MyProfile)

