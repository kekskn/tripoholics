from django.contrib import admin
from .models import MyUser, AddPastTravel, AddFutureTravel, MyProfile


admin.site.register(MyUser)
admin.site.register(MyProfile)
admin.site.register(AddPastTravel)
admin.site.register(AddFutureTravel)

