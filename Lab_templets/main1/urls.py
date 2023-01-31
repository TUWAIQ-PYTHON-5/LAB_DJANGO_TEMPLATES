from django.urls import path
from. import views


app_name = "main"

urlpatterns = [
    path('today/', views.date_tody, name="date_tody"),
    path('random/password/',views.get_random, name = "paasword"),
    path('favs/games/',views.fav_games, name = "fav game")
]