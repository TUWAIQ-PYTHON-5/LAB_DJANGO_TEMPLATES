from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from datetime import date
import random
import string


# Create your views here.

def today_date(request : HttpRequest):
   
    context = {
        
        "today" : date.today()
    }
    return render(request , "main/index.html", context)


def fav_games(request : HttpRequest):
    list_game = ["God of War (PlayStation Hits)" , "Horizon Forbidden West ","Call of Duty: Modern Warfare II"]
    context = {
    
        "list_game": list_game

    }
    return render( request , "main/fav_games.html", context )



def random_password(request :HttpRequest):
    
    # get random string of length 6 without repeating letters
    result_str = ''.join(random.sample(string.ascii_lowercase, 8))
    context = {
        
        "password" : result_str

    }
    return render(request , "main/password.html",context)





