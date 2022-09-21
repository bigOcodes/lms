from django.contrib import messages
from django.shortcuts import render
from .models import *
from .serializers import BookSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
# Create your views here.

def Index(request):
    return render(request, 'Index.html')

'''
django-rest api Documentation
BooksAPI - use to fetch all books and using GET method for fetching data

url - api/books/
'''

@api_view(['GET'])
def BooksAPI(request):
    books = Books.objects.all().order_by('id')
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

'''
BooksDetailsAPI - use to fetch a book by id and using GET method for fetching data. for e.g., booksDetailsAPI/1/
url api/books/<int:id>/
'''
@api_view(['GET'])
def BooksDetailsAPI(request, id):
    books = get_object_or_404(Books, id=id)
    serializer = BookSerializer(books, many=False)
    return Response(serializer.data, status=status.HTTP_200_OK)

'''
AddBooksAPI - use to add book to database and using POST method for post a data into database
url - api/books/add/
'''
@api_view(['POST'])
def AddBooksAPI(request):
    serializer = BookSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

'''
EditBookAPI - use to update existing data in database
url - api/books/edit/<int:id>/
'''

@api_view(['PUT'])
def EditBookAPI(request, id):
    books = get_object_or_404(Books, id=id)
    serializer = BookSerializer(books, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    print(request.data)
    return Response(serializer.errors, status=status.HTTP_304_NOT_MODIFIED)

'''
DeleteBookAPI - use to delete data from database
url - api/books/delete/<int:id>/
'''

@api_view(['DELETE'])
def DeleteBookAPI(request, id):
    books = get_object_or_404(Books, id=id)
    if books:
        books.delete()
        return Response('Product successfully Deleted!', status=status.HTTP_200_OK)

    return Response("That Product Doesn't Exists!", status=status.HTTP_204_NO_CONTENT)


def home(request):
    books = Books.objects.all()
    return render(request, 'studentView.html', {'books':books})

'''
login function - 
requesting for email and password from form in login.html file which is present inside templates folder.
    email = request.POST['email']
    password = request.POST['password']
    
validating using email and password whether this data is present inside database or not.
ob = Admin.objects.get(email = email, password = password)
is present will return a boolean value True or False.
if true -> render to index page
else -> it will show an error
'''

def login(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        try:
            ob = Admin.objects.get(email = email, password = password)
            if ob:
                return render(request, 'Index.html')
        except:
            messages.error(request, "Invalid email or password! or Not exist. SignUp your account first!")
    return render(request, 'login.html')


'''
signup function - 
requesting for name, email and password from form in signup.html file which is present inside templates folder.
    name = request.POST['name']
    email = request.POST['email']
    password = request.POST['password']
    
validating using email and name whether this data is exist inside database or not if 
exist will raise an error data already exist if not then create the profile using name, email and password.
'''

def signup(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        if Admin.objects.filter(name = name) or Admin.objects.filter(email = email):
            messages.error(request, 'Name or Email already exist! try different name or Email')
        else:
            ob = Admin.objects.create(name = name, email = email, password = password)
            ob.save()
            messages.success(request, 'Profile Added Succefully')
    return render(request, 'signup.html')