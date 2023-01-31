from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path("today/", views.today_date, name="today_date"),
    path("favs/games/", views.fav_games, name="fav_games"),
    path("random/password/", views.random_password, name="password"),


]