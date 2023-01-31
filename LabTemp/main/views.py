from django.shortcuts import render
from django.http import HttpResponse,HttpRequest
from datetime import date
import secrets
import string


def todate(request : HttpRequest):
    result = date.today()
    return render(request,'main/index.html',{'date_today':result})

def generat_password(request : HttpRequest):
    letters = string.ascii_letters
    digits = string.digits
    special_chars = string.punctuation
    mix_pwd = letters + digits + special_chars
    length_pwd = 12
    generat_pwd = ''
    for x in range(length_pwd):
        generat_pwd += ''.join(secrets.choice(mix_pwd))
    result = generat_pwd
    return render(request,'main/generat_password.html',{'password':result})

def fav_game(request : HttpRequest):
    result = 'The witcher'
    return render(request,'main/fav_game.html',{'result':result})

