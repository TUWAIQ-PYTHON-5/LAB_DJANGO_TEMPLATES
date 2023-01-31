from django.urls import path
from . import views

app_name = "dateapp"

urlpatterns = [
    path("today/", views.today_page, name="today_page"),
    path("random/", views.random_pass, name="randompass_page"),
    path("fav/", views.favoritlist, name="fav_page") 

]