from django.contrib import messages
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from library_app.forms import ModelAuthor,ModelBook,ModelGenre
from library_app.models import Author,Book,Genre

# Create your views here.

def redirect_to_book_name(request):
    
        return redirect('index', filter='book_name')
    
def index(request,filter):
    books=Book.objects.order_by(filter)
    paginator=Paginator(books,6)
    
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request,'library_app/index.html',{'page_obj':page_obj})

def add_genre(request):
    genre=Genre.get_model_name(Genre())
    if request.method=='POST':
        form=ModelGenre(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")
    form=ModelGenre()
    return render(request,'library_app/add.html',{"form":form,'model_name':genre})

def add_author(request):
    author=Author.get_model_name(Author())
    if request.method=='POST':
        form=ModelAuthor(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")
    form=ModelAuthor()
    return render(request,'library_app/add.html',{"form":form,'model_name':author})


def add_book(request):
    book=Book.get_model_name(Book())
    if request.method=='POST':
        form=ModelBook(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:

            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")
    form=ModelBook()
    return render(request,'library_app/add.html',{"form":form,'model_name':book})


def single_book(request,id):
    obj=get_object_or_404(Book,pk=id)
    return render(request,'library_app/each.html',{'obj':obj})

def single_author(request,id):
    obj=get_object_or_404(Author,pk=id)
    return render(request,'library_app/each.html',{'obj':obj})
