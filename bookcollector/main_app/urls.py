from django.urls import path
from . import views

urlpatterns = [
    # home page views
    path('', views.home, name='home'),
]