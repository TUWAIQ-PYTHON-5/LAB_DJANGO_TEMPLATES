from django.urls import path
from . import views


urlpatterns =[
    
    path("today/", views.today, name="today"),
    path("random/password/", views.generate_pass , name=""),
    path("favs/games/", views.favorite_games , name="")
]