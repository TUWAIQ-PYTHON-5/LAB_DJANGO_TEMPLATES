from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from datetime import date
import random

# Create your views here.
def date_pag(request :HttpRequest):
    context = {
        'today' : date.today()
            }
    return render(request, "main/today.html",context)

def random_pass_page(request :HttpRequest):
    random_pass=random.choices(["a","d","g","6","9","&"],k=15)
    print(random_pass)
    random_pass_string="".join(random_pass) 
    return render(request, "main/password.html",{"password":random_pass_string})


def Far_gmas(request :HttpRequest):
    favorite =[ 'slither','Pubg' ]
    context={'favorite':favorite}
    
    return render(request, "main/gams.html",context)



