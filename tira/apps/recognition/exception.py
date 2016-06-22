from django.http import HttpResponse


class HttpResponseUnsupportedMediaType(HttpResponse):
    status_code = 415