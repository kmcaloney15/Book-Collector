from django.urls import path
from . import views

urlpatterns = [
    # home page views
    path('', views.home, name='home'),
    # about path
    path('about/', views.about, name='about'),
    # books path 
    path('books/', views.books_index, name='index'),
    path('books/<int:book_id>/', views.books_detail, name='detail'),
    path('books/create/', views.BookCreate.as_view(), name='books_create'),
    path('books/<int:pk>/update/', views.BookUpdate.as_view(), name='books_update'),
    path('books/<int:pk>/delete/', views.BookDelete.as_view(), name='books_delete'),
    path('books/<int:book_id>/add_review/', views.add_review, name='add_review'),

     path('fandom/', views.FandomList.as_view(), name='fandom_index'),
    path('fandom/<int:pk>/', views.FandomDetail.as_view(), name='fandom_detail'),
    path('fandom/create/', views.FandomCreate.as_view(), name='fandom_create'),
    path('fandom/<int:pk>/update/', views.FandomUpdate.as_view(), name='fandom_update'),
    path('fandom/<int:pk>/delete/', views.FandomDelete.as_view(), name='fandom_delete'),


    path('books/<int:book_id>/assoc_fandom/<int:fandom_id>/', views.assoc_fandom, name='assoc_fandom'),
]