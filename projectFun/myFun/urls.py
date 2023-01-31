from django.urls import path
from . import views

app_name = "myFun"

urlpatterns = [
    path("", views.today_date, name="today"),
    path("random/password/", views.random_pass, name="password"),
    path("favs/games/", views.fov_Games, name="mygames"),
]

