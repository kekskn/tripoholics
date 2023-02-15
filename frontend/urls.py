from django.urls import path
from . import views

from chat import views as chatViews

urlpatterns = [
    path('', views.index, name="index"),
    # path('my_messages', views.my_messages, name="messages"),
    path('my_messages/', views.my_messages, name="messages"),
    # path("<str:room_name>/", chatViews.index, name="room"),
    # path("<str:room_name>/", views.my_messages, name="room"),
]