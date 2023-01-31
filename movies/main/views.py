from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from datetime import date
from password_generator import PasswordGenerator

# Create your views here.

def get_homepage(request : HttpRequest) :
    return render(request, "main/homepage.html")

def get_datePage(request : HttpRequest) :
    context = {
        "today" : date.today()
    }
    return render(request, "main/date.html", context)

def get_FavoriteGames(request : HttpRequest) :
    return render(request, "main/FavoriteGames.html")


def get_Password(request : HttpRequest) :
    context = {
        "password" : PasswordGenerator().generate()
    }
    return render(request, "main/Password.html", context)

