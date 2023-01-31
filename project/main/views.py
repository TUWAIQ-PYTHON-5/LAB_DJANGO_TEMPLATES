from django.shortcuts import render
from django.http import HttpRequest , HttpResponse
from datetime import date
from random import random

# Create your views here.

def index(request : HttpRequest):
    context={
        "today":date.today()
    }

    return render(request , "main/index.html", context)


def random_password(request):
    context={
        "pass":random
    }
    return render(request,"main/pass.html",context  )


def games(request):
    context={
        "games":"FIFA"
    }

    return render(request,"main/game.html",context)