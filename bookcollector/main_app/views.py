from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Book
from .forms import ReviewForm
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
    review_form = ReviewForm()
    return render(request, 'books/detail.html', {'book': book, 'review_form': review_form})

def add_review(request, book_id):
    # create a ModelForm instance using the data in request.POST
  form = ReviewForm(request.POST)
  # validate the form
  if form.is_valid():
    # don't save the form to the db until it
    # has the book_id assigned
    new_review = form.save(commit=False)
    new_review.book_id = book_id
    new_review.save()
  return redirect('detail', book_id=book_id)


#  ---- CLASSES -----------------------------

class BookCreate(CreateView):
    model = Book
    fields = '__all__'
    # fields = ['name', 'author', 'series', 'description'],
    # success_url = '/books/',


class BookUpdate(UpdateView):
  model = Book
  fields = ['author', 'series', 'description']

class BookDelete(DeleteView):
  model = Book
  success_url = '/books/'