from django.views.decorators.http import require_http_methods
from django.http import JsonResponse
from .detection import Detector
from .models import Photo
from .http_responses import HttpResponseUnsupportedMediaType, HttpResponseNotAcceptable

CLASSIFICATION_THRESHOLD = 0.2


@require_http_methods('POST')
def images(request):
    if 'image' not in request.FILES:
        return HttpResponseNotAcceptable()
    image = request.FILES['image']
    if not is_image_valid(image):
        return HttpResponseUnsupportedMediaType()
    photo = store_photo(photo=image, folder='tmp')
    classification = get_classification(photo)
    if is_classification_good_enough(value=float(classification['0']['score']), threshold=CLASSIFICATION_THRESHOLD):
        store_photo(photo=image, folder=classification['0']['label'].replace(" ", "_"), )
    photo.delete()
    return JsonResponse(classification)


def store_photo(photo, folder):
    photo = Photo(photo=photo, folder=folder)
    photo.save()
    return photo


def get_classification(photo):
    detector = Detector(file_path=photo.photo.path)
    return detector.run()


def is_classification_good_enough(value, threshold):
    return value >= threshold


def is_image_valid(image):
        return image.content_type == 'image/jpeg'
