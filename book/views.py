from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import Book
from django.urls import reverse
from .forms import BookForm

# Create your views here.
def all_books(request):
    books = Book.objects.all()
    form = BookForm()
    return render(request, 'books/allBooks.html', {
        "books": books,
        "form":form
    })

#process books add
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            desc = form.cleaned_data['description']
            year = form.cleaned_data['year']
            book = Book.objects.create(title=title, description=desc, year=year)
            book.save()
            return HttpResponseRedirect(reverse('books'))
        else:
            return render(request, 'books/allBooks.html', {
                "message":"me le falto algo"
            })
            

            
    