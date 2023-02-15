from django.urls import path
from . import views

urlpatterns = [
    path('login_user', views.login_user, name="login"),
    path('logout_user', views.logout_user, name="logout"),
    path('register_user', views.register_user, name="register"),
    path('myprofile', views.myprofile, name="myprofile"),
    path('add_travel_page', views.add_travel_page, name="add_travel_page"),
    ]
