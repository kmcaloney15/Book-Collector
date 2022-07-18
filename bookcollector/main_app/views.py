from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

#  Home View
def home(request):
    return HttpResponse('Home Page')

# About View
def about(request):
    return render(request, 'about.html')