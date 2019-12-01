import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from todos.models import Todo
from todos.serializers import TodoSerializer


client = Client()


class GetAllTodosTest(TestCase):
    """ Test module for GET all todos API """

    def setUp(self):
        Todo.objects.create(
            title='Test Title',
            description='Testing!')
        Todo.objects.create(
            title='Another Test Title',
            description='Testing, testing, 123!')

    def test_get_all_todos(self):
        response = client.get(reverse('get_post_todos'))
        todos = Todo.objects.all()
        serializer = TodoSerializer(todos, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
