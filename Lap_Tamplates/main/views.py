from django.shortcuts import render
from django.http import HttpRequest , HttpResponse
from datetime import date
import random
import string , numbers

# Create your views here.


def today (request : HttpRequest):
    context = {
        "today" : date.today
    }

    return render(request ,"main/today.html",context)


def random_password (request : HttpRequest):
    
     # get random string of length 6 without repeating letters
    result_str = ''.join(random.sample(string.ascii_lowercase, 8))
    context = {"password" : result_str

    }

    return render(request,"main/password.html",context)


def favs_games(request : HttpRequest):
    
    return render(request ,"main/games.html")