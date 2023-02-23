from django.urls import re_path, path
from clientApi import views
from .views import MessageView, DialogView, CurrentUserView

urlpatterns = [
    # re_path(r'^messages$', views.messagesApi),
    path('messages/', MessageView.as_view()),
    path('dialogs/', DialogView.as_view()),
    path('current_user/', CurrentUserView.as_view()),
]