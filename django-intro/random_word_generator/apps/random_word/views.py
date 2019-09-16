from django.shortcuts import render, HttpResponse , redirect
from django.utils.crypto import get_random_string

def index(request):
    if request.method == "POST":
        if 'counter' not in request.session:
            request.session['counter'] = 0 
        else:
            request.session['counter'] += 1
        request.session['random'] = get_random_string(length=14)
    return render( request,"random_word/index.html")

def reset(request):
    request.session['counter'] = 0 
    return redirect("/")
    
