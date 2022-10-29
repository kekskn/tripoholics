from django.urls import path
from .views import MyUserView

urlpatterns = [
    path('home', MyUserView.as_view()),
]