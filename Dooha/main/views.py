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
   
    return render( request , "main/fav_games.html" )



def random_password(request :HttpRequest):
    

    result = ''.join(random.sample(string.ascii_lowercase, 8))
    context = {
        
        "password" : result

    }
    return render(request , "main/password.html",context)





