from django.urls import path
from . import views

app_name="main"

urlpatterns=[
    path("tody/",views.date_tody,name="date_tody"),
    path("random/password/",views.rand_pass,name="random"),
    path("favs/games/",views.the_favtiote_games,name="favoritegames")

]