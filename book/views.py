from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import Book
from django.urls import reverse
from .forms import BookForm, CommentForm

# Create your views here.
def all_books(request):
    books = Book.objects.all()
    form = BookForm()
    return render(request, 'books/allBooks.html', {
        "books": books,
        "form":form
    })

#process comment add
def single_book(request, book_id):
    form = CommentForm()
    book = Book.objects.get(id=book_id) 
    comments = book.comments.all()
    return render(request, 'books/bookComments.html', {
        "book":book,
        "comments": comments,
        'form':form
    })

def add_book_comment(request, book_id):
    book = Book.objects.get(id=book_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.book = book
            comment.user = form.cleaned_data['user']
            comment.comment = form.cleaned_data['comment']
            comment.save()
            return HttpResponseRedirect(reverse('single_book', args=[book_id]))
    else:
        return HttpResponseRedirect(reverse('single_book', args=[book_id]))

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
            

            
    