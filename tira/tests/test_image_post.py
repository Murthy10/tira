import os
from django.test import TestCase, Client


class ImagePostTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_image_post(self):
        pwd = os.path.dirname(os.path.realpath(__file__))
        file_path = pwd + '/images/blume.jpg'
        url = '/recognition/images'
        data = {'image': open(file_path, 'rb')}
        response = self.client.post(url, data, format='multipart')
        self.assertEquals(response.status_code, 200)

    def test_no_image(self):
        url = '/recognition/images'
        data = {'file': b'test'}
        response = self.client.post(url, data, format='multipart')
        self.assertEquals(response.status_code, 406)

    def test_no_valid_image(self):
        pwd = os.path.dirname(os.path.realpath(__file__))
        file_path = pwd + '/files/test.txt'
        url = '/recognition/images'
        data = {'image': open(file_path, 'rb')}
        response = self.client.post(url, data, format='multipart')
        print(response.content)
        self.assertEquals(response.status_code, 415)