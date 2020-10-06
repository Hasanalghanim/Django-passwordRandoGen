from django.forms.widgets import PasswordInput
from django.http import request
from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.

def home(request):
    return render(request, 'generator/home.html')





def password(request):
    chers = list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('uppercase'):
        chers.extend(list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
    if request.GET.get('special'):
        chers.extend(list("!@#$%&"))
    if request.GET.get('numbers'):
        chers.extend(list("1234567890"))
    
    
    length = int(request.GET.get('length', 12))
    
    thepassword = ''
    
    for x in range(length):
    
        thepassword += random.choice(chers)
    
    return render(request, 'generator/password.html', {'password': thepassword})


