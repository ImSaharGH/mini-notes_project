from django.test import TestCase
from django.shortcuts import reverse
from .models import Notes

class NotesListViewTest(TestCase):
    def setUp(self):
        self.note_obj = Notes.objects.create(author= 'sahar' , text = 'Sample text')
       

    def test_notes_listt_view_test(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code , 200)

    def test_notes_list_test_url_by_name(self):
        response = self.client.get(reverse('Notes_list'))
        self.assertEqual(response.status_code , 200)

    def test_notes_list_page(self):
        response = self.client.get(reverse('Notes_list'))
        self.assertContains(response , self.note_obj.text)
