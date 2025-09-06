from django.test import TestCase
from django.urls import reverse
from datetime import date
from .models import Book


class BookTests(TestCase):
    def setUp(self):
        self.book = Book.objects.create(
            title='Test Book',
            author='Author',
            published_date=date(2020, 1, 1),
            isbn='1234567890123',
            description='Desc',
        )

    def test_book_list(self):
        response = self.client.get(reverse('book_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Book')

    def test_book_detail(self):
        response = self.client.get(reverse('book_detail', args=[self.book.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Author')

    def test_book_create(self):
        response = self.client.post(
            reverse('book_add'),
            {
                'title': 'New Book',
                'author': 'New Author',
                'published_date': '2021-01-01',
                'isbn': '9876543210123',
                'description': 'New description',
            },
        )
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Book.objects.filter(title='New Book').exists())

    def test_book_update(self):
        response = self.client.post(
            reverse('book_edit', args=[self.book.pk]),
            {
                'title': 'Updated Book',
                'author': 'Author',
                'published_date': '2020-01-01',
                'isbn': '1234567890123',
                'description': 'Desc',
            },
        )
        self.assertEqual(response.status_code, 302)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, 'Updated Book')

    def test_book_delete(self):
        response = self.client.post(reverse('book_delete', args=[self.book.pk]))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Book.objects.filter(pk=self.book.pk).exists())
