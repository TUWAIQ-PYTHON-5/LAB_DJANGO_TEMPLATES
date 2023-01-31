from django.shortcuts import render
from datetime import date
from django.http import HttpRequest,HttpResponse
import random
import string


def today_date(request : HttpRequest):
    
    context = { "today" : date.today()

    }
    
    return render(request , "myFun/todaydate.html" , context)

def random_pass(request :HttpRequest):
    
    # get random string of length 6 without repeating letters
    result_str = ''.join(random.sample(string.ascii_lowercase, 8))
    context = {"password" : result_str

    }
    return render(request , "myFun/randompass.html",context)

def fov_Games(request :HttpRequest):
    myGames = ["game1" , "game2","game3"]
    context = {
        "mygames":myGames
    }
    return render(request , "myFun/FovGames.html",context)

