from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from datetime import date
import random
import string
# Create your views here.


def index(request : HttpRequest):
    tagLine = "You have reached to the right palce for fun"
    context = {
        "tagLine" : tagLine,
    }
    return render(request , "main/index.html", context)


######################################

def today (request : HttpRequest):
    context = {
        "today" : date.today()
    }
    return render(request , "main/today.html", context)
######################################
def password (request : HttpRequest):

    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    num = string.digits
    symbols = string.punctuation
    all = lower + upper + num + symbols
    temp = random.sample(all,8)
    password = "".join(temp)
    all = string.ascii_letters + string.digits + string.punctuation
    password = "".join(random.sample(all,8))

    context = {
        "password" : "Your New Password is: " + password
    }
    return render(request , "main/password.html", context)
####################################
def fvList (request : HttpRequest):

    myFavGames:list = ['Last of Us', 'Fifa23', 'ResidantEvil']

    context = {
       "myFavGames" : myFavGames
    }
    return render(request , "main/games.html", context)