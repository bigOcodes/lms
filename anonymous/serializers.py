from .models import *
from rest_framework import serializers

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = '__all__'  # taking all fields ('title','category','author','price')