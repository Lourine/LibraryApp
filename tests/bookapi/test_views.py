from django.http import response
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from LibraryApp.book.models import Book


class BookAPITestCase(APITestCase):

    def create_book(self):
        sample_book = {'title': "Hello", "desc": "Test"}
        response = self.client.post(reverse('todos'), sample_book)
        return response

    def authenticate(self):
        self.client.post(reverse("register"), {
                         'username': "username", "email": "email@gmail.com", "password": "password"})

        response = self.client.post(
            reverse('login'), {"email": "email@gmail.com", "password": "password"})

        self.client.credentials(
            HTTP_AUTHORIZATION=f"Bearer {response.data['token']}")


class TestListCreateBooks(BookAPITestCase):

    def test_should_not_create_book_with_no_auth(self):
        response = self.create_book()
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_should_create_book(self):
        previous_book_count = Book.objects.all().count()
        self.authenticate()

        response = self.create_todo()
        self.assertEqual(Book.objects.all().count(), previous_book_count+1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['title'], 'Hello')
        self.assertEqual(response.data['desc'], 'Test')

    def test_retrieves_all_books(self):
        self.authenticate()
        response = self.client.get(reverse('books'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data['results'], list)

        self.create_book()
        res = self.client.get(reverse('todos'))
        self.assertIsInstance(res.data['count'], int)
        self.assertEqual(res.data['count'], 1)


class TestTodoDetailAPIView(BookAPITestCase):

    def test_retrieves_one_item(self):
        self.authenticate()
        response = self.create_todo()

        res = self.client.get(
            reverse("book", kwargs={'id': response.data['id']}))

        self.assertEqual(res.status_code, status.HTTP_200_OK)

        book = Book.objects.get(id=response.data['id'])

        self.assertEqual(book.title, res.data['title'])

    def test_updates_one_item(self):
        self.authenticate()
        response = self.create_book()

        res = self.client.patch(
            reverse("book", kwargs={'id': response.data['id']}), {
                "title": "New one", "description": "Favorite"
            })

        self.assertEqual(res.status_code, status.HTTP_200_OK)

        updated_book = Book.objects.get(id=response.data['id'])
        self.assertEqual(updated_book.descriprition, 'Favorite')
        self.assertEqual(updated_book.title, 'New one')

    def test_deletes_one_item(self):
        self.authenticate()
        res = self.create_book()
        prev_db_count = Book.objects.all().count()

        self.assertGreater(prev_db_count, 0)
        self.assertEqual(prev_db_count, 1)

        response = self.client.delete(
            reverse("book", kwargs={'id': res.data['id']}))

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        self.assertEqual(Book.objects.all().count(), 0)
