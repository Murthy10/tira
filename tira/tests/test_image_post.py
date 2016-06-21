import os
from django.test import TestCase, Client


class ImagePostTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_image_post(self):
        pwd = os.path.dirname(os.path.realpath(__file__))
        print(pwd)
        file_path = pwd + '/images/blume.jpg'
        url = '/recognition/images'
        data = {'file': open(file_path, 'rb')}
        response = self.client.post(url, data, format='multipart')
        print(response.content)
        self.assertEquals(response.status_code, 200)