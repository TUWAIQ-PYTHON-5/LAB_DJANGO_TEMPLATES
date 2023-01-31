from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path("",views.get_homepage),
    path("today/",views.get_datePage, name="date_page"),
    path("random/password/", views.get_Password, name="password_page"),
    path("favs/games/", views.get_FavoriteGames, name="FavoriteGames_page")
]