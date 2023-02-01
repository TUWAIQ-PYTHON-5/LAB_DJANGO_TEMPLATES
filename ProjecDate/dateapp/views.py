from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from datetime import date
import random
import string
# Create your views here.


def today_page(request : HttpRequest):
    today = date.today()
    context ={"today": today}
    return render(request , "dateapp/today.html", context)


def random_pass(request :HttpRequest):
    random_pass= random.choice(string.ascii_letters + string.digits+string.punctuation)
    random_pass_string = "".join(random_pass)
    return render(request, "dateapp/randompass.html", {'password': random_pass_string})


def favoritlist(request: HttpRequest):

    return render(request,'dateapp/fav.html')