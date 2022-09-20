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

@api_view(['GET'])
def BooksAPI(request):
    books = Books.objects.all().order_by('id')
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def BooksDetailsAPI(request, id):
    books = get_object_or_404(Books, id=id)
    serializer = BookSerializer(books, many=False)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def AddBooksAPI(request):
    serializer = BookSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def EditBookAPI(request, id):
    books = get_object_or_404(Books, id=id)
    serializer = BookSerializer(books, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    print(request.data)
    return Response(serializer.errors, status=status.HTTP_304_NOT_MODIFIED)

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