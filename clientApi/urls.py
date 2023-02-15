from django.urls import re_path
from clientApi import views

urlpatterns = [
    re_path(r'^messages$', views.messagesApi),

]