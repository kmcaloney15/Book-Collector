from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Book, Fandom
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
    fandom = Fandom.objects.all()
    id_list = book.fandom.all().values_list('id')
    # Now we can query for Fandoms whose ids are not in the list using exclude
    fandom_book_doesnt_have = Fandom.objects.exclude(id__in=id_list)
    review_form = ReviewForm()
    return render(request, 'books/detail.html', {'book': book, 'review_form': review_form, 'fandom': fandom_book_doesnt_have})



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

def assoc_fandom(request, book_id, fandom_id):
  # Note that you can pass a Fandom's id instead of the whole Fandom object
  Book.objects.get(id=book_id).fandom.add(fandom_id)
  return redirect('detail', book_id=book_id)



#  ---- CLASSES -----------------------------

class BookCreate(CreateView):
    model = Book
    # fields = '__all__'
    fields = ['name', 'author', 'series', 'description'],
    # success_url = '/books/',


class BookUpdate(UpdateView):
  model = Book
  fields = ['author', 'series', 'description']

class BookDelete(DeleteView):
  model = Book
  success_url = '/books/'


class FandomList(ListView):
  model = Fandom


class FandomDetail(DetailView):
  model = Fandom


class FandomCreate(CreateView):
  model = Fandom
  fields = '__all__'
#   fields = ['name', 'description']
  success_url = '/fandom/'

class FandomUpdate(UpdateView):
  model = Fandom
  fields = ['name', 'description']
  success_url = '/fandom/'


class FandomDelete(DeleteView):
  model = Fandom
  success_url = '/books/'
