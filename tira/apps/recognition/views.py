from django.views.decorators.http import require_http_methods
from django.http import JsonResponse
from django.http import UnreadablePostError
from .detection import Detector
from .models import Photo


@require_http_methods('POST')
def images(request):
    file = request.FILES['file']
    image = Photo(photo=file, folder='tmp')
    image.save()
    detector = Detector(file_path=image.photo.path)
    answers = detector.run()
    image.delete()
    stored_folder = answers['0']['label'].replace(" ", "_")
    Photo(photo=file, folder=stored_folder).save()
    return JsonResponse(answers)

def validate_file_extension(value):
    if value.file.content_type != 'image/jpag':
        return False
    return True