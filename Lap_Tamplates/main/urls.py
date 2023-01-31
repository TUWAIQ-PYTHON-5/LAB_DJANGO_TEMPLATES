from django.urls import path
from . import views


app_name ="main"

urlpatterns= [
    path("today/",views.today ,name= "today_page"),
    path("random/password/",views.random_password , name="random_pass_page"),
    path("favs/games/",views.favs_games, name="f_games_page")    
]