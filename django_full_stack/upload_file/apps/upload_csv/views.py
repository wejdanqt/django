from django.shortcuts import render , redirect 
from django.contrib import messages
from .models import names
import re
# Create your views here.

def index(request):
    return render(request, "upload_csv/upload.html")


def upload_csv(request):
    if request.method == "POST":
        csv_file = request.FILES["csv_file"]
        if not csv_file.name.endswith('.csv'):
            print("not CSV")
            messages.error(request,'File is not CSV type. Please upload a CSV file')
            return redirect("/")
         
        else:
            file_data = csv_file.read().decode("utf-8")	
            lines = file_data.split("\n")
            for line in lines:						
                fields = line.split(",")
                f = re.sub('\W+',' ', fields[0] )
                names.objects.create(name= f )
            return redirect("/")



