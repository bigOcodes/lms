from . import views
from django.urls import path

urlpatterns = [
    path('index/', views.Index, name="Index"),

    # restAPI urls
    path('api/books/', views.BooksAPI, name="BooksAPI"),
    path('api/books/add/', views.AddBooksAPI, name="AddBooksAPI"),
    path('api/books/<int:id>/', views.BooksDetailsAPI, name="BooksDetailsAPI"),
    path('api/books/edit/<int:id>/', views.EditBookAPI, name="EditBookAPI"),
    path('api/books/delete/<int:id>/', views.DeleteBookAPI, name="DeleteBookAPI"),

    # home, login and signup urls
    path('', views.home, name="home"),
    path('login/', views.login, name="login"),
    path('signup/', views.signup, name="signup"),
]