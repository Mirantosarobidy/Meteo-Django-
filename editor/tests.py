from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import Editor

class BlogTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username = 'testuser',
            email = 'test@email.com',
            password = 'secret'
        )
        
        self.editor = Editor.objects.create(
            title = 'Date',
            body = 'Nice day',
            author = self.user,
        )
        
    def test_string_representation(self):
        post = Editor(title = 'A sample title')
        self.assertEqual(str(post), post.title)
        
    def test_post_content(self):
        self.assertEqual(f'{self.editor.title}', 'Date')
        self.assertEqual(f'{self.editor.author}', 'testuser')
        self.assertEqual(f'{self.editor.body}', 'Nice day')
        
    def test_post_list_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Nice day')
        self.assertTemplateUsed(response, 'home.html')
        
    def test_editor_detail_view(self):
        response = self.client.get('/editor/1/')
        no_response = self.client.get('/post/100000/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'Date')
        self.assertTemplateUsed(response, 'editor_detail.html')

    def test_editor_create_view(self):
        response = self.client.post(reverse('edit_new'), {
            'title' : 'New title',
            'body' : 'New text',
            'author' : self.user.id,
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Editor.objects.last().title, 'New title')
        self.assertEqual(Editor.objects.last().body, 'New text')
        
    def test_editor_update_view(self):
        response = self.client.post(reverse('editor_edit', args='1'),{
            'title' : 'Updated title',
            'body' : 'Update text'
        })
        self.assertEqual(response.status_code, 302)
        
    def test_editor_delete_view(self):
        response = self.client.post(
            reverse('editor_delete', args='1'))
        self.assertEqual(response.status_code, 302)