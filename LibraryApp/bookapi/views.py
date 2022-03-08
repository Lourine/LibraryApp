from django_filters.rest_framework.backends import DjangoFilterBackend
from LibraryApp.book.models import Book
from rest_framework import permissions, filters
from . serializers import BookSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from . pagination import CustomPageNumberPagination


class BookAPIView(ListCreateAPIView):
    serializer_class = BookSerializer
    pagination_class = CustomPageNumberPagination
    permission_classes = (IsAuthenticated,)
    

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)

    def get_queryset(self):
        return Book.objects.filter(owner=self.request.user)


class BookDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = BookSerializer
    permission_classes = (IsAuthenticated,)
    lookup_field = "id"

    def get_queryset(self):
        return Book.objects.filter(owner=self.request.user)
