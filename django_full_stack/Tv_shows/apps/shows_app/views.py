from django.shortcuts import render
from .models import shows

def all_shows(request):
    context = {
        "shows" : shows.objects.all()
    }		
    return render(request, "shows_app/shows.html", context)
