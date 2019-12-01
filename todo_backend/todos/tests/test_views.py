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


class GetSingleTodoTest(TestCase):
    """ Test module for GET single todo API """

    def setUp(self):
        self.test_list_1 = Todo.objects.create(
            title='Test Title',
            description='Testing!')
        self.test_list_2 = Todo.objects.create(
            title='Another Test Title',
            description='Testing, testing, 123!')

    def test_get_valid_single_todo(self):
        response = client.get(
            reverse('get_delete_update_todo', kwargs={'pk': self.test_list_1.pk}))
        todo = Todo.objects.get(pk=self.test_list_1.pk)
        serializer = TodoSerializer(todo)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_single_todo(self):
        response = client.get(
            reverse('get_delete_update_todo', kwargs={'pk': 30}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class CreateNewTodoTest(TestCase):
    """ Test module for inserting a new todo """

    def setUp(self):
        self.valid_payload = {
            "title": "Working Testlist!",
            "description": "A descriptive description of the list!",
            "entries": [
                {
                    "text_entry": "Test1",
                    "completed": False
                },
                {
                    "text_entry": "Test number two",
                    "completed": True
                },
                {
                    "text_entry": "3",
                    "completed": False
                }
            ]
        }
        self.invalid_payload = {
            "title": ""
        }

    def test_create_valid_todo(self):
        response = client.post(
            reverse('get_post_todos'),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        todo = Todo.objects.get(pk=1)
        serializer = TodoSerializer(todo)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_todo(self):
        response = client.post(
            reverse('get_post_todos'),
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class UpdateSingleTodoTest(TestCase):
    """ Test module for updating an existing todo record """

    def setUp(self):
        self.test_list_1 = Todo.objects.create(
            title='Test Title',
            description='Testing!')
        self.test_list_2 = Todo.objects.create(
            title='Another Test Title',
            description='Testing, testing, 123!')
        self.valid_payload = {
            "title": "Working Testlist!",
            "description": "A descriptive description of the list!",
            "entries": [
                {
                    "text_entry": "Test1",
                    "completed": False
                },
                {
                    "text_entry": "Test number two",
                    "completed": True
                },
                {
                    "text_entry": "3",
                    "completed": False
                }
            ]
        }
        self.invalid_payload = {
            "title": ""
        }

    def test_valid_update_todo(self):
        response = client.put(
            reverse('get_delete_update_todo', kwargs={'pk': self.test_list_1.pk}),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_update_todo(self):
        response = client.put(
            reverse('get_delete_update_todo', kwargs={'pk': self.test_list_2.pk}),
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class DeleteSingleTodoTest(TestCase):
    """ Test module for deleting an existing todo record """

    def setUp(self):
        self.test_list_1 = Todo.objects.create(
            title='Test Title',
            description='Testing!')
        self.test_list_2 = Todo.objects.create(
            title='Another Test Title',
            description='Testing, testing, 123!')

    def test_valid_delete_todo(self):
        response = client.delete(
            reverse('get_delete_update_todo', kwargs={'pk': self.test_list_1.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_delete_todo(self):
        response = client.delete(
            reverse('get_delete_update_todo', kwargs={'pk': 30}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
