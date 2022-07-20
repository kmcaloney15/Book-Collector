from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Book
# Create your views here.


#  --- DEFINE VIEWS -----------------------------


#  Home View
def home(request):
    return HttpResponse('Home Page')

# About View


def about(request):
    return render(request, 'about.html')


# Books Index View
def books_index(request):
    books = Book.objects.all()
    return render(request, 'books/index.html', {'books': books})


def books_detail(request, book_id):
    book = Book.objects.get(id=book_id)
    return render(request, 'books/detail.html', {'book': book})


#  ---- CLASSES -----------------------------

class BookCreate(CreateView):
    model = Book
    fields = '__all__'
    # fields = ['name', 'author', 'series', 'description'],
    # success_url = '/books/',


class BookUpdate(UpdateView):
  model = Book
  fields = ['name', 'author', 'series', 'description']

class BookDelete(DeleteView):
  model = Book
  success_url = '/books/'