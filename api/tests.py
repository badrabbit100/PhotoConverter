from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from main.models import Photo
from PIL import Image
import tempfile
import io


def generate_photo_file():
    """ Generate random .png image file """

    file = io.BytesIO()
    image = Image.new('RGBA', size=(300, 300), color=(155, 0, 0))
    image.save(file, 'png')
    file.name = 'test.png'
    file.seek(0)
    return file


class PhotoTests(APITestCase):

    @staticmethod
    def generate_random_file():
        """ Generate random with byte-file """
        # create a temporary file and write some data to it
        fp = tempfile.TemporaryFile()
        fp.write(b'Hello guys!')
        # read data from file
        fp.seek(0)
        fp.read()
        b'Hello guys!'
        # close the file, it will be removed
        return fp

    def setUp(self):
        """ Create test objects and define URL for API testing """
        # self.test_image_file = tempfile.NamedTemporaryFile(suffix=".jpg")
        self.test_photo = Photo.objects.create(photo_input=str(generate_photo_file()))
        self.test_photo2 = Photo.objects.create(photo_input=str(generate_photo_file()))

        # URL for testing
        self.test_create_url = reverse('photos')
        self.test_delete_url = reverse('delete_all')

    def test_create_photo(self):
        """ Upload a photo test """

        photo_file = generate_photo_file()
        data = {'photo_input': photo_file, 'action': ''}
        response = self.client.post(self.test_create_url, data, format='multipart')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Photo.objects.all().count(), 3)

    def test_get_photo_lists_of_owner(self):
        """ Ensure we can get Photo list """

        data = {}
        response = self.client.get(self.test_create_url, data, format='json')
        self.assertEqual(Photo.objects.all().count(), 2)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_can_not_create_photo_with_wrong_format(self):
        """ Ensure we can not upload file with non-image format """

        photo_file = self.generate_random_file()
        data = {'photo_input': photo_file, 'action': ''}
        response = self.client.post(self.test_create_url, data, format='multipart')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Photo.objects.all().count(), 2)

    def test_create_photo_with_rotation(self):
        """ Ensure we can not upload file with non-image format """

        photo_file = self.generate_random_file()
        data = {'photo_input': photo_file, 'action': ''}
        response = self.client.post(self.test_create_url, data, format='multipart')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Photo.objects.all().count(), 2)

    def test_delete_all_photos(self):
        """ Ensure we delete all photos """

        data = {}
        response = self.client.post(self.test_delete_url, data, format='multipart')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Photo.objects.all().count(), 0)
