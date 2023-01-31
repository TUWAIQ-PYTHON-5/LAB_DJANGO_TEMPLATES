from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path("", views.index, name="home_page"),
    path("today/", views.today, name="today"),
    path("random/password/", views.password, name="new_password"),
    path("favs/games/", views.fvList, name="my_games")
    
]