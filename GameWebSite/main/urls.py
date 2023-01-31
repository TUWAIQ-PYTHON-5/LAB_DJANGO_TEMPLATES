from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path("", views.main_page, name="main_page"),
    path("today/", views.today_page, name="today_page"),
    path("random/password/", views.password_page, name="random_password_page"),
    path("favs/games/", views.games_page, name="favs_games_page"),
]