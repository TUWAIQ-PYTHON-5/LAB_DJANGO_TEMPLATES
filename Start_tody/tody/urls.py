from django.urls import path
from . import views
app_name = "today"

urlpatterns = [
    path("today/", views.date, name="today_page"),
    path("random/password/", views.password, name="random_page"),
    path("favs/games/", views.games, name="favs_page")
]