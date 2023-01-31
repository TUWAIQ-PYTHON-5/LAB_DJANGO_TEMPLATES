from django.urls import path
from . import views

app_name = "first_app"

urlpatterns = [
   path("today/",views.today, name="page 1"),
   path("random/password/",views.random_pass, name="page 2"),
   path("favs/games/",views.fav_games, name="page 3"),
]