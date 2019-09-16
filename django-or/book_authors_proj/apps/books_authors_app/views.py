from django.shortcuts import render	, redirect
from .models import authors , books

#Book 
def index(request):
    context = {
        "books" : books.objects.all()
    }		
    return render(request, "books_authors_app/index.html", context)

def add(request):
    if request.method == "POST":
        request.POST['title']
        books.objects.create(title=request.POST['title'] , desc = request.POST['dec'] )
    return redirect("/")

def view(request , id):
    book = books.objects.get(id= id)
    context = {
        "authors": authors.objects.all(),
        "book" : book,
        "book_authors" : book.author.all()
    }
    return render(request, "books_authors_app/book_detail.html", context)

def add_author(request , id):
    if request.method == "POST":
         book = books.objects.get(id= id)
         author_id = request.POST['add_authors']
         book.author.add(author_id)
         print(author_id)
    return redirect('/view/%d'%int(id))


#-------------------------------------------------------
#Author 

def index2(request):
    context = {
        "authors" : authors.objects.all()
    }		
    return render(request, "books_authors_app/index2.html", context)

def add_an_author(request):
    if request.method == "POST":
        authors.objects.create(first_name=request.POST['first_name'] , last_name = request.POST['last_name'],
        notes = request.POST['note'] )
    return redirect("/authors")

def view_an_author(request , id):
    author = authors.objects.get(id= id)
    context = {
        "author" : author,
        "author_books" : author.books.all(),
        "books" : books.objects.all()
    }
    return render(request, "books_authors_app/author_detail.html", context)

def add_book(request , id):
    if request.method == "POST":
        author = authors.objects.get(id= id)
        book_id = request.POST['add_book']
        author.books.add(book_id)
    return redirect('/view_an_author/%d'%int(id))

