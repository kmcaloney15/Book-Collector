from django.urls import path
from . import views

urlpatterns = [
    # home page views
    path('', views.home, name='home'),
    # about path
    path('about/', views.about, name='about'),
    # books path 
    path('books/', views.books_index, name='index'),
    path('books/<int:book_id>/', views.books_detail, name='detail')
]