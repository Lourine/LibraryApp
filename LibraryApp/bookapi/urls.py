from . views import BookAPIView, BookDetailAPIView
from django.urls import path

urlpatterns = [
    path("", BookAPIView.as_view(), name="books"),
    path("<int:id>", BookDetailAPIView.as_view(), name="book")
]
