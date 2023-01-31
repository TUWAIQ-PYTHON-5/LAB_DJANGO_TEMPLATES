from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from datetime import date
import random

# Create your views here.

def date_page(request : HttpRequest):
    context ={
    "today" : date.today()}
    
    return render(request , "main/today.html", context)



def random_password_page(request : HttpRequest):
    random_pass=random.choices(["a","b","c","4","5","&"],k=15)
    print(random_pass)
    random_pass_string="".join(random_pass)
    return render(request , "main/randomPassword.html", {"password":random_pass_string})





def fav_games(request : HttpRequest):
    Game = 'Billiards'
    return render(request, "main/games.html",{"fav":Game} )


