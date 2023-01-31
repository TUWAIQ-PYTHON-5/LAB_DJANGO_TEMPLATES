from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path("", views.date_page, name="date_page"),
    path("randomPassword/", views.random_password_page, name="random_page"),
    path("games/", views.fav_games, name="games_page")
]