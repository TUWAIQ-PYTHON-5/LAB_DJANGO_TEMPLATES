from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path("", views.index, name="today"),
    path("random/password/",views.random_password,name="random password"),
    path("favs/games/",views.games,name="game")
]