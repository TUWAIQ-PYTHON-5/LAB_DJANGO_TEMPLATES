from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from datetime import date
import random

# Create your views here.

def today(request : HttpRequest):
    
    context = {
       
        "today" : date.today()
    }
    return render(request , "main/index.html", context)


def generate_pass(request : HttpRequest):

    char = "AaBbCcDdEeFfJjHhIiGgKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz"
    num = "1234567890"
    cod = "!@#$%^&*()"
    password = ""
    for i in range(9):  

         res = random.choice(char+num+cod)
         password += res

    context = {
        "password" : password
    }
   
    return render(request, "random/password.html" ,  context)

def favorite_games(request : HttpRequest):
    games = ["Call of duty " , "Dark Souls " , "Elden Ring"]
    result = " "
    for i in games:  
         result += i
    context = {
        "result" : result
    }
    return render(request, "favs/games.html" ,  context)

