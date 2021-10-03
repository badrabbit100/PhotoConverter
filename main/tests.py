from django.test import TestCase
from django.urls import reverse
from main.models import Photo
from api.tests import generate_photo_file


class TestViews(TestCase):

    def setUp(self):
        self.photo = Photo.objects.create(photo_input=str(generate_photo_file()))
        self.test_url = reverse('index')
        self.test_upload_photo_url = reverse('photo_upload')
        # self.test_delete_photo_url = reverse('photo_delete')

    def test_project_list(self):
        """ Test rendering main page """

        response = self.client.get(self.test_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/index.html')

    def test_upload_new_photo(self):
        photo_file = generate_photo_file()
        data = {'file': photo_file, 'action': ''}

        response = self.client.post(self.test_upload_photo_url, data, format='multipart')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Photo.objects.all().count(), 2)

    def test_create_photo_without_data(self):
        """ Try to create photo without data """
        data = {}
        response = self.client.post(self.test_upload_photo_url, data, format='multipart')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Photo.objects.all().count(), 1)
