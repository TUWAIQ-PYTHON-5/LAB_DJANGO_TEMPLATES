from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from datetime import date
import random
import string
# Create your views here.

def today(request:HttpRequest):
    context = {
      
        "today" : date.today()
    }
    return render(request , "first_app/page1.html", context)

def random_pass(request:HttpRequest):
 random_num = random.choices(string.ascii_letters+string.digits,k=15)
 listToStr = ''.join(random_num)
 context = {
        "random_password":listToStr
        }



 return render(request , "first_app/page2.html",context)


def fav_games(request:HttpRequest):

 
 return render(request , "first_app/page3.html")    