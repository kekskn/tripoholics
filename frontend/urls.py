from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('my_messages', views.my_messages, name="messages"),

]