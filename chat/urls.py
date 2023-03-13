# chat/urls.py
from django.urls import path

from . import views

# from ..frontend.views import my_messages
from frontend import views as frontViews

urlpatterns = [
    # path("", views.index, name="index"),
    path("", frontViews.my_messages, name="index"),
    path("<str:room_name>/", views.room, name="room"),
    path("new_dialog/<str:room_name>/", views.room, name="room"),
    # path("<str:room_name>/", views.room, name="room"),
]