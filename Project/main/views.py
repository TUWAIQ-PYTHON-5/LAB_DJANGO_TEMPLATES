from django.shortcuts import render
from django.http import HttpRequest,HttpResponse
from datetime import date
import random
import string
# Create your views here.
def today_page(request:HttpRequest):
    today=date.today()
    context = { "today" : date.today() }
    return render(request,"main/index.html",context)
def passward_page(request:HttpRequest):
    context=random.choices(["k","P","i"],k=15)
    print(context)
    random_pass_string="".join(context)
    return render(request,"main/random_passward.html",{"passward":random_pass_string})
def games_page(request:HttpRequest):
    return render(request,"main/games.html")