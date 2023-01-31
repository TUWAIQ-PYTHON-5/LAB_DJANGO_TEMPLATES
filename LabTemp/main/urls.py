from . import views
from django.urls import path

urlpatterns = [
    
    path('today/', views.todate, name='todate'),
    path('random/password/',views.generat_password,name='generat_password'),
    path('favs/games/',views.fav_game,name='fav_game'),


]