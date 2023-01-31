from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from datetime import date
import random


def today_page(request : HttpRequest):
    headLine = "This is Asrar News Page  "
    context = {
        "headLine" : headLine,
        "today" : date.today()
    }
    return render(request , "asrar_news/today_page.html", context)


def random_password(request : HttpRequest):
    random_pass = random.choices(["k","a","d","1","2","3","4"], k=15)
    random_pass_string = "".join(random_pass)
    return render(request, "asrar_news/random_password.html", {"password":random_pass_string})


def fav_games(request : HttpRequest):
    return render(request, "asrar_news/fav_games.html",)
