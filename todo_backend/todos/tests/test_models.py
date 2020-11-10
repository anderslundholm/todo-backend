from django.test import TestCase
from todos.models import Todo, Entry


class TodoTest(TestCase):
    """ Test module for Todo model. """

    def setUp(self):
        self.test_list_1 = Todo.objects.create(
            title='Test Title',
            description='Testing!')
        self.test_list_2 = Todo.objects.create(
            title='Test Title Number Two',
            description='Testing, testing, 123')
        self.entry_1 = Entry.objects.create(
            text_entry='Test1',
            todo=self.test_list_1)
        self.entry_2 = Entry.objects.create(
            text_entry='Test2',
            todo=self.test_list_1)
        self.entry_3 = Entry.objects.create(
            text_entry='Test3',
            todo=self.test_list_1)

    def test_description(self):
        title_1 = Todo.objects.get(title='Test Title')
        title_2 = Todo.objects.get(title='Test Title Number Two')
        self.assertEqual(
            title_1.get_description(), 'Testing!')
        self.assertEqual(
            title_2.get_description(), 'Testing, testing, 123')
    
    def test_get_all_entries(self):
        todo_list = Todo.objects.get(pk=self.test_list_1.pk)
        all_entries = todo_list.entries.all()
        self.assertEqual(list(all_entries),
                         [self.entry_1,
                          self.entry_2,  
                          self.entry_3])


class EntryTest(TestCase):
    """ Test module for Entry model. """

    def setUp(self):
        self.test_list = Todo.objects.create(
            title='Test Title',
            description='Testing!')
        self.entry_1 = Entry.objects.create(
            text_entry='Test1',
            todo=self.test_list)
        self.entry_2 = Entry.objects.create(
            text_entry='Test2',
            todo=self.test_list)
        self.entry_3 = Entry.objects.create(
            text_entry='Test3',
            todo=self.test_list)

    def test_entries(self):
        test_entry_1 = Entry.objects.get(pk=self.entry_1.pk)
        test_entry_2 = Entry.objects.get(pk=self.entry_2.pk)
        self.assertEqual(
            test_entry_1.get_text_entry(), 'Test1')
        self.assertEqual(
            test_entry_2.get_text_entry(), 'Test2')
