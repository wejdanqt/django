from django.shortcuts import render	, redirect
import random
def index(request):
    if 'your_gold' not in request.session:
        request.session['your_gold'] = 0 
    if 'act' not in request.session:
        request.session['act'] = ''

    return render(request, "prosess_money/index.html")

def prosess_money(request):
    if request.method == "POST":
        if request.POST['building'] == 'farm':
            rand =  random.randint(10, 20) 
            request.session['your_gold'] += rand 
            request.session['act'] += "Earned "+ str(rand )+" golds form the "+request.POST['building']+"\n"
        if request.POST['building'] == 'cave':
            rand =  random.randint(5, 10) 
            request.session['your_gold'] += rand 
            request.session['act'] += "Earned "+ str(rand )+" golds form the "+request.POST['building']+"\n"
        if request.POST['building'] == 'house':
            rand =  random.randint(2, 5) 
            request.session['your_gold'] += rand 
            request.session['act'] += "Earned "+ str(rand )+" golds form the "+request.POST['building']+"\n"
        if request.POST['building'] == 'casino':
            rand =  random.randint(-50, 50) 
            request.session['your_gold'] += rand 
            if(rand > 0):
                request.session['act'] += "Earned "+ str(rand )+" golds form the "+request.POST['building']+"\n"
            else:
                request.session['act'] += "Enterd  a "+request.POST['building']+ " and lost"+ str(rand )+"...Ouch \n"
    return redirect('/')
    
    
    




