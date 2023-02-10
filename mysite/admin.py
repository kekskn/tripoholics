from django.contrib import admin
from .models import MyUser, AddTravel, MyProfile


admin.site.register(MyUser)
admin.site.register(MyProfile)
admin.site.register(AddTravel)

