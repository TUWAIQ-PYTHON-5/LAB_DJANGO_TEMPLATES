from django.urls import path
from . import views
app_name="main"
urlpatterns=[
    path("today/",views.today_page,name="today_page"),
    path("random/password/",views.passward_page,name="passward_page"),
    path("favs/games/",views.games_page,name="games_page"),

]