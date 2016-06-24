from django.http import HttpResponse


class HttpResponseUnsupportedMediaType(HttpResponse):
    def __init__(self, content=b'', *args, **kwargs):
        super(HttpResponseUnsupportedMediaType, self).__init__(*args, **kwargs)
        self.content = [b'<h1>Only image/jpeg supported!</h1>']
    status_code = 415


class HttpResponseNotAcceptable(HttpResponse):
    def __init__(self, content=b'', *args, **kwargs):
        super(HttpResponseNotAcceptable, self).__init__(*args, **kwargs)
        self.content = [b'<h1>No image file!</h1>']
    status_code = 406
