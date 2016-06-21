from django.db import models


def image_path(instance, filename):
    return 'images/{0}/{1}'.format(instance.folder, filename)


class Photo(models.Model):
    folder = models.TextField()
    photo = models.ImageField(upload_to=image_path)