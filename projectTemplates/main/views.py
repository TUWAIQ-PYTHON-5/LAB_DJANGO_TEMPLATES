from django.shortcuts import render
from django.http import HttpRequest,HttpResponse
from datetime import date
from random import random

# Create your views here.
def date_tody(request):
 context={
    "tody":date.today()
} 

 return render(request,"main/tody.html",context)

def rand_pass(request):
    context={
        "password": random    
    }
    return render(request,"main/random.html",context)

def the_favtiote_games(request):
    context={
        "games":"football"
    }
    return render(request,"main/favoritegames.html",context)