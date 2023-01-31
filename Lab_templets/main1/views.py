from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from datetime import date
import random
import string
# Create your views here.


def date_tody(request : HttpRequest):
   
    context = {
        "today" : date.today()
    }
    return render(request , "main/index.html", context)




def get_random(request: HttpRequest):

    resulte = ''.join(random.choices(string.ascii_letters ,k = 8 ) )
    context = { "password": resulte }
    
    return render (request, "main/pass.html", context  )




def fav_games(request: HttpRequest):

    resulte = {"fav-Game1","fav-Game2","fav-Game3"}
    
    context = { "gems": resulte }
    
    return render (request, "main/game.html", context  )



    

