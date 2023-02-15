# chat/views.py
from django.shortcuts import render

from frontend import views as frontViews

def index(request):
    return render(request, "chat/index.html")


def room(request, room_name):
    print('room_name', room_name)
    # return render(request, "chat/room.html", {"room_name": room_name})
    # return render(request, "frontend/messages.html", {"room_name": room_name})
    return frontViews.my_messages(request, room_name)