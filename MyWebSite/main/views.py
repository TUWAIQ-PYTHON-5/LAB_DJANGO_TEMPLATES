from django.shortcuts import render
from django.http import HttpRequest
from datetime import date
import random
import string
# Create your views here.


def today_page(request : HttpRequest):
    
    context = {
      
        "today" : date.today()
    }
    return render(request , "main/today.html", context)

def games_page(request:HttpRequest):
    context ={
        'game1' :"Domino",
        'game2' : "Uno",
        'game3' :"Crash"
    }
    return render(request , "main/faves.html", context)

   
def random_password(request :HttpRequest):

   
    result = ''.join(random.sample(string.ascii_lowercase, 8))
    context = {

        "password" : result

    }
    return render(request , "main/random.html",context)