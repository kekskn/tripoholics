from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.safestring import mark_safe
import json

# Create your views here.
def index(request, *args, **kwargs):
    return render(request, 'frontend/index.html')

@login_required
def my_messages(request, room_name, *args, **kwargs):
    print('my_messages from frontend/views.py')
    return render(request, 'frontend/messages.html', {"room_name": room_name, 'username': request.user.username})
