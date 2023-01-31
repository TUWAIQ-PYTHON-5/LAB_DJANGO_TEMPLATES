from django.urls import path
from . import views


app_name = 'main'

urlpatterns=[
    path("", views.today_page, name="today_page"),
    path("random/password/", views.random_password, name = "password_page"),
    path("favs/games/", views.games_page, name="game_page")
]