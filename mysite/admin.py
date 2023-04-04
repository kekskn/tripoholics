from django.contrib import admin
from .models import AddPastTravel, AddFutureTravel, MyProfile

admin.site.register(MyProfile)
admin.site.register(AddPastTravel)
admin.site.register(AddFutureTravel)
