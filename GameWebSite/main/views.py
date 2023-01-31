from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from datetime import date
from random import randrange
# Create your views here.


def main_page(request : HttpRequest):

    return render(request, "main/index.html")

def today_page(request : HttpRequest):
    context = {
        "today" : date.today()
    }
    return render(request , "main/today.html", context)

def password_page(request : HttpRequest):
    context = {
        "randomNumber" : randrange(100000,999999)
    }

    return render(request, "main/password.html",context)

def games_page(request : HttpRequest):

    return render(request, "main/games.html")