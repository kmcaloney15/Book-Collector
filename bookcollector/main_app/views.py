from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

#  Home View
def home(request):
    return HttpResponse('Home Page')