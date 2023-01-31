from django.shortcuts import render
from django.http import HttpRequest,HttpResponse
from datetime import  date
import random
import string

# Create your views here.
def date(request : HttpRequest):
    context={"today" : date.today()}
    return render(request,"Start_tody/index.html", context)

def password(request : HttpRequest):
    random_pass = random.choices(string.ascii_letters + string.digits + string.punctuation, k=15)
    random_pass_string = "".join(random_pass)
    return render(request,"Start_tody/index2.html", {"passwrd",random_pass_string})

def games(request : HttpRequest):
    return render(request,"Start_tody/index3.html")

