from django.urls import path
from . import views

app_name = "asrar_news"

urlpatterns = [
    path("today_page/", views.today_page, name="today_page"),
    path("random/password/", views.random_password, name="random_password"),
    path("fav/games/", views.fav_games, name="fav_games")
    

]