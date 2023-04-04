from django.urls import path
from . import views

urlpatterns = [
    path('login_user', views.login_user, name="login"),
    path('logout_user', views.logout_user, name="logout"),
    path('register_user', views.register_user, name="register"),
    path('update_user', views.update_user, name="update_user"),
    path('myprofile', views.myprofile, name="myprofile"),
    path('add_travel_page', views.add_travel_page, name="add_travel_page"),
    path('add_past_trip', views.add_past_trip, name="add_past_trip"),
    path('add_next_trip', views.add_next_trip, name="add_next_trip"),
]
