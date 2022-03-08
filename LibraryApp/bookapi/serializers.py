from ..book.models import Book
from rest_framework import fields
from rest_framework.serializers import ModelSerializer


class BookSerializer(ModelSerializer):
    class Meta:
        model = Book
        fields = ('id', 'name', 'author', 'email', 'describe')
